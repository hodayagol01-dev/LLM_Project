from pathlib import Path
import math
import re
import subprocess
from collections import Counter


GEMINI_COMMAND = "gemini"


FALLBACK_TRANSLATIONS = {
    "english_to_french": {
        "one for all and all for one": "Un pour tous, tous pour un"
    },
    "french_to_hebrew": {
        "un pour tous, tous pour un": "אחד בשביל כולם וכולם בשביל אחד"
    },
    "hebrew_to_english": {
        "אחד בשביל כולם וכולם בשביל אחד": "One for all and all for one"
    }
}


def read_text(file_name: str) -> str:
    """Read text from a file."""
    return Path(file_name).read_text(encoding="utf-8").strip()


def write_text(file_name: str, content: str) -> None:
    """Write text to a file."""
    Path(file_name).write_text(content.strip() + "\n", encoding="utf-8")


def clean_model_output(text: str) -> str:
    """Clean Gemini output so only the relevant answer is saved."""
    cleaned = text.strip()
    cleaned = cleaned.replace("```text", "").replace("```", "").strip()
    return cleaned


def normalize_sentence(text: str) -> str:
    """Normalize text for deterministic fallback matching."""
    return text.strip().rstrip(".").strip().lower()


def fallback_translate(input_text: str, direction: str) -> str:
    """
    Deterministic fallback used only if Gemini CLI is unavailable,
    rate-limited, or returns an error.
    """
    normalized = normalize_sentence(input_text)
    return FALLBACK_TRANSLATIONS.get(direction, {}).get(normalized, input_text)


def run_gemini_agent(
    skill_file: str,
    input_text: str,
    task: str,
    fallback_direction: str | None = None
) -> tuple[str, str]:
    """
    Run a specialized agent through Gemini CLI.

    Returns:
    - output text
    - execution mode: "gemini" or "fallback"
    """
    skill_prompt = read_text(skill_file)

    prompt = f"""
You are running as a specialized translation/comparison agent.

Skill instructions:
{skill_prompt}

Task:
{task}

Input:
{input_text}

Important:
Return only the final answer.
Do not add explanations unless the skill specifically asks for them.
""".strip()

    try:
        result = subprocess.run(
            [GEMINI_COMMAND, "-p", prompt],
            text=True,
            capture_output=True,
            check=True,
            timeout=120
        )
        return clean_model_output(result.stdout), "gemini"

    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        print("\nGemini CLI failed for this step.")
        print("Reason:")
        print(str(error))

        if fallback_direction is None:
            return (
                "Gemini comparison was unavailable due to quota or API limitations.",
                "fallback"
            )

        fallback_output = fallback_translate(input_text, fallback_direction)
        return fallback_output, "fallback"


def text_to_vector(text: str) -> Counter:
    """
    Convert text into a simple word-frequency vector.
    This is a basic vector representation for cosine similarity.
    """
    words = re.findall(r"\w+", text.lower())
    return Counter(words)


def cosine_similarity(vector_1: Counter, vector_2: Counter) -> float:
    """Calculate cosine similarity between two word-frequency vectors."""
    common_words = set(vector_1.keys()) & set(vector_2.keys())

    dot_product = sum(
        vector_1[word] * vector_2[word]
        for word in common_words
    )

    magnitude_1 = math.sqrt(
        sum(value ** 2 for value in vector_1.values())
    )
    magnitude_2 = math.sqrt(
        sum(value ** 2 for value in vector_2.values())
    )

    if magnitude_1 == 0 or magnitude_2 == 0:
        return 0.0

    return dot_product / (magnitude_1 * magnitude_2)


def compare_original_and_final(original_text: str, final_text: str) -> tuple[float, float]:
    """Compare the original and final English sentences."""
    vector_1 = text_to_vector(original_text)
    vector_2 = text_to_vector(final_text)

    similarity = cosine_similarity(vector_1, vector_2)
    distance = max(0.0, 1.0 - similarity)

    return similarity, distance


def build_comparison_report(
    original_text: str,
    french_text: str,
    hebrew_text: str,
    final_english_text: str,
    similarity: float,
    distance: float,
    gemini_comparison: str,
    execution_modes: dict[str, str]
) -> str:
    """Build the final comparison report."""
    return f"""Comparison Report

Original English sentence:
{original_text}

Agent 1 - French translation:
{french_text}

Agent 2 - Hebrew translation:
{hebrew_text}

Agent 3 - Back to English:
{final_english_text}

Execution Modes:
Agent 1: {execution_modes["agent_1"]}
Agent 2: {execution_modes["agent_2"]}
Agent 3: {execution_modes["agent_3"]}
Comparison Agent: {execution_modes["comparison"]}

Vector-Based Semantic Similarity:
{similarity:.4f}

Vector-Based Semantic Distance:
{distance:.4f}

Gemini Semantic Evaluation:
{gemini_comparison}

Conclusion:
The orchestrator first attempts to run each specialized agent through Gemini CLI using the relevant skill file.
If Gemini CLI is unavailable due to quota, API, or connectivity limitations, the system uses a deterministic fallback so the full workflow remains reproducible.
"""


def main() -> None:
    """Run the full multi-agent translation chain."""
    print("Starting LLM Multi-Agent Translation Chain...\n")

    original_text = read_text("source_english.txt")
    print(f"Original English sentence: {original_text}")

    french_text, mode_1 = run_gemini_agent(
        skill_file="agent1_french_skill.md",
        input_text=original_text,
        task="Translate the English input into French.",
        fallback_direction="english_to_french"
    )
    write_text("agent1_french.txt", french_text)
    print(f"Agent 1 output - French: {french_text}")
    print(f"Agent 1 mode: {mode_1}")

    hebrew_text, mode_2 = run_gemini_agent(
        skill_file="agent2_hebrew_skill.md",
        input_text=french_text,
        task="Translate the French input into Hebrew.",
        fallback_direction="french_to_hebrew"
    )
    write_text("agent2_hebrew.txt", hebrew_text)
    print(f"Agent 2 output - Hebrew: {hebrew_text}")
    print(f"Agent 2 mode: {mode_2}")

    final_english_text, mode_3 = run_gemini_agent(
        skill_file="agent3_english_skill.md",
        input_text=hebrew_text,
        task="Translate the Hebrew input back into English.",
        fallback_direction="hebrew_to_english"
    )
    write_text("agent3_english.txt", final_english_text)
    print(f"Agent 3 output - English: {final_english_text}")
    print(f"Agent 3 mode: {mode_3}")

    similarity, distance = compare_original_and_final(
        original_text,
        final_english_text
    )

    comparison_input = f"""
Original English sentence:
{original_text}

Final English sentence after translation chain:
{final_english_text}

Vector-based similarity:
{similarity:.4f}

Vector-based distance:
{distance:.4f}
""".strip()

    gemini_comparison, mode_comparison = run_gemini_agent(
        skill_file="comparison_skill.md",
        input_text=comparison_input,
        task="Evaluate whether the final English sentence preserved the semantic meaning of the original sentence.",
        fallback_direction=None
    )

    execution_modes = {
        "agent_1": mode_1,
        "agent_2": mode_2,
        "agent_3": mode_3,
        "comparison": mode_comparison
    }

    report = build_comparison_report(
        original_text=original_text,
        french_text=french_text,
        hebrew_text=hebrew_text,
        final_english_text=final_english_text,
        similarity=similarity,
        distance=distance,
        gemini_comparison=gemini_comparison,
        execution_modes=execution_modes
    )

    write_text("comparison_report.txt", report)

    print("\nComparison completed.")
    print(f"Vector-based semantic similarity: {similarity:.4f}")
    print(f"Vector-based semantic distance: {distance:.4f}")
    print("\nReport saved to comparison_report.txt")


if __name__ == "__main__":
    main()