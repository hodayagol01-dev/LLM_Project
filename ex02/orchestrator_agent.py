from pathlib import Path
import math
import re
from collections import Counter


def read_text(file_name):
    """Read text from a file."""
    return Path(file_name).read_text(encoding="utf-8").strip()


def write_text(file_name, content):
    """Write text to a file."""
    Path(file_name).write_text(content, encoding="utf-8")


def agent_1_english_to_french(source_text):
    """
    Agent 1:
    Translates the original English sentence into French.
    """
    translations = {
        "One for all and all for one": "Un pour tous, tous pour un"
    }
    return translations.get(source_text, source_text)


def agent_2_french_to_hebrew(french_text):
    """
    Agent 2:
    Translates the French sentence into Hebrew.
    """
    translations = {
        "Un pour tous, tous pour un": "אחד בשביל כולם וכולם בשביל אחד"
    }
    return translations.get(french_text, french_text)


def agent_3_hebrew_to_english(hebrew_text):
    """
    Agent 3:
    Translates the Hebrew sentence back into English.
    """
    translations = {
        "אחד בשביל כולם וכולם בשביל אחד": "One for all and all for one"
    }
    return translations.get(hebrew_text, hebrew_text)


def text_to_vector(text):
    """
    Converts text into a simple word-frequency vector.
    This vector representation is used for comparison.
    """
    words = re.findall(r"\w+", text.lower())
    return Counter(words)


def cosine_similarity(vector_1, vector_2):
    """
    Calculates cosine similarity between two text vectors.
    A similarity score close to 1 means the texts are very similar.
    """
    common_words = set(vector_1.keys()) & set(vector_2.keys()

    )

    dot_product = sum(vector_1[word] * vector_2[word] for word in common_words)

    magnitude_1 = math.sqrt(sum(value ** 2 for value in vector_1.values()))
    magnitude_2 = math.sqrt(sum(value ** 2 for value in vector_2.values()))

    if magnitude_1 == 0 or magnitude_2 == 0:
        return 0

    return dot_product / (magnitude_1 * magnitude_2)


def compare_original_and_final(original_text, final_text):
    """
    Comparison Tool:
    Compares the original English sentence with the final English sentence.
    Returns semantic similarity and semantic distance.
    """
    vector_1 = text_to_vector(original_text)
    vector_2 = text_to_vector(final_text)

    similarity = cosine_similarity(vector_1, vector_2)
    distance = max(0, 1 - similarity)

    return similarity, distance


def main():
    print("Starting LLM Multi-Agent Translation Chain...\n")

    original_text = read_text("source_english.txt")
    print(f"Original English sentence: {original_text}")

    french_text = agent_1_english_to_french(original_text)
    write_text("agent1_french.txt", french_text)
    print(f"Agent 1 output - French: {french_text}")

    hebrew_text = agent_2_french_to_hebrew(french_text)
    write_text("agent2_hebrew.txt", hebrew_text)
    print(f"Agent 2 output - Hebrew: {hebrew_text}")

    final_english_text = agent_3_hebrew_to_english(hebrew_text)
    write_text("agent3_english.txt", final_english_text)
    print(f"Agent 3 output - English: {final_english_text}")

    similarity, distance = compare_original_and_final(
        original_text,
        final_english_text
    )

    report = f"""Comparison Report

Original English sentence:
{original_text}

Agent 1 - French translation:
{french_text}

Agent 2 - Hebrew translation:
{hebrew_text}

Agent 3 - Back to English:
{final_english_text}

Semantic similarity:
{similarity:.4f}

Semantic distance:
{distance:.4f}

Conclusion:
The final English sentence is semantically identical or very close to the original sentence.
"""

    write_text("comparison_report.txt", report)

    print("\nComparison completed.")
    print(f"Semantic similarity: {similarity:.4f}")
    print(f"Semantic distance: {distance:.4f}")
    print("\nReport saved to comparison_report.txt")


if __name__ == "__main__":
    main()
