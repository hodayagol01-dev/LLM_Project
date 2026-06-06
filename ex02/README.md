# Assignment 2 – Multi-Agent Translation Chain

## Project Overview

This folder contains the solution for Assignment 2 in the LLM course.

The project implements a multi-agent translation chain. The system starts with an English sentence, translates it through several languages, and then translates it back to English.

The translation flow is:

```text
English → French → Hebrew → English
```

After the translation chain is completed, the final English sentence is compared to the original English sentence in order to evaluate how much meaning was preserved.

---

## Assignment Context

This assignment is based on the L05 lesson about AI agent infrastructure, prompt engineering, tokens, vectors, embeddings, tools, memory, and skills.

The main goal is to demonstrate how an AI workflow can be divided into several specialized agents or skills.

Each step in the chain has a specific role:

1. Translate from English to French.
2. Translate from French to Hebrew.
3. Translate from Hebrew back to English.
4. Compare the original English sentence with the final English sentence.

This structure follows the idea of using different skills as specialized “costumes” for the agent.

---

## Translation Chain

The translation chain is:

```text
source_english.txt
→ agent1_french.txt
→ agent2_hebrew.txt
→ agent3_english.txt
→ comparison_report.txt
```

The purpose of this chain is to simulate a “broken telephone” process and then evaluate whether the original meaning survived the translations.

---

## Files in This Folder

```text
ex02/
├── source_english.txt
├── agent1_french.txt
├── agent2_hebrew.txt
├── agent3_english.txt
├── comparison_report.txt
├── agent1_french_skill.md
├── agent2_hebrew_skill.md
├── agent3_english_skill.md
├── comparison_skill.md
├── orchestrator_agent.py
└── README.md
```

### File Descriptions

- `source_english.txt` – the original English sentence.
- `agent1_french.txt` – the French translation output.
- `agent2_hebrew.txt` – the Hebrew translation output.
- `agent3_english.txt` – the final English translation output.
- `comparison_report.txt` – the semantic comparison result.
- `agent1_french_skill.md` – the English-to-French translation skill.
- `agent2_hebrew_skill.md` – the French-to-Hebrew translation skill.
- `agent3_english_skill.md` – the Hebrew-to-English translation skill.
- `comparison_skill.md` – the semantic comparison skill.
- `orchestrator_agent.py` – the script that manages the full translation chain.

---

## Skills

This assignment uses skill-style Markdown files to define specialized agent roles.

Each skill represents a different responsibility in the translation chain:

| Skill File | Role |
|---|---|
| `agent1_french_skill.md` | English to French translator |
| `agent2_hebrew_skill.md` | French to Hebrew translator |
| `agent3_english_skill.md` | Hebrew to English translator |
| `comparison_skill.md` | Semantic comparison between the original and final English sentences |

The use of separate skill files helps show how one agentic workflow can be divided into smaller expert roles.

---

## Orchestrator Agent

The file `orchestrator_agent.py` represents the orchestration layer.

Its role is to manage the chain from beginning to end:

1. Read the original sentence from `source_english.txt`.
2. Use the first translation step to create the French version.
3. Use the second translation step to create the Hebrew version.
4. Use the third translation step to translate the Hebrew sentence back to English.
5. Run the comparison step.
6. Save the comparison result in `comparison_report.txt`.

This demonstrates a higher-level agent that coordinates multiple specialized skills instead of treating each file as an unrelated manual script.

---

## Semantic Comparison

The comparison step evaluates how much meaning was preserved after the translation chain.

The goal is not only to compare the exact words, but to compare the semantic meaning of the original English sentence and the final English sentence.

The comparison report is saved in:

```text
comparison_report.txt
```

This step is connected to the L05 concepts of vectors, embeddings, and semantic distance.

---

## Example Input / Output

### Original Input

```text
One for all and all for one.
```

### Translation Flow

```text
English → French → Hebrew → English
```

### Expected Behavior

The final English sentence should preserve the meaning of the original sentence, even if the wording changes slightly.

For example, the final sentence may not be exactly identical word-for-word, but it should remain semantically close to the original.

### Output Files

After running the chain, the project produces:

```text
agent1_french.txt
agent2_hebrew.txt
agent3_english.txt
comparison_report.txt
```

The final report explains whether the meaning was preserved across the translation chain.

---

## How to Run

From the `ex02` folder, run:

```bash
python orchestrator_agent.py
```

The orchestrator runs the translation chain and updates the output files.

After running the script, check:

```text
agent1_french.txt
agent2_hebrew.txt
agent3_english.txt
comparison_report.txt
```

---

## Research and Analysis

During the development process, the project explored how meaning can change when a sentence passes through multiple translation agents.

The main analytical questions were:

1. Does the final English sentence preserve the same meaning as the original sentence?
2. Which translation step changes the sentence the most?
3. Can a semantic comparison identify meaning preservation better than a literal word comparison?
4. How can specialized skill files improve the quality and consistency of each translation step?

The comparison stage was added to make the assignment analytical, not only technical.

---

## Design Decisions

### 1. Separate Skill Files

Each translation direction has its own skill file. This keeps the instructions focused and makes each agent role clear.

### 2. Orchestrator Script

Instead of running all translation steps manually, the orchestrator manages the full process.

This makes the project closer to an agentic workflow.

### 3. Semantic Comparison

The final comparison focuses on meaning preservation rather than exact wording.

This is important because translations may change grammar, word order, or phrasing while still preserving the original idea.

---

## Current Limitations

The current implementation demonstrates the required workflow, but it still has limitations:

1. The translation quality depends on the clarity of the skill instructions.
2. The semantic comparison is documented through the comparison report.
3. More advanced embedding-based metrics, such as cosine similarity, could be added in a future version.
4. The project currently focuses on one translation chain.
5. Additional languages could be added later.

---

## Future Improvements

Possible future improvements include:

1. Add automatic embedding generation for the original and final English sentences.
2. Calculate cosine similarity between the original and final sentence embeddings.
3. Add more test sentences.
4. Compare several language chains.
5. Add a summary table of semantic similarity scores.
6. Turn the workflow into a fully automated multi-agent pipeline.

---

## Project Status

The project includes:

- A multi-agent translation chain.
- Dedicated skill files for each translation role.
- An orchestrator script.
- Input and output text files.
- A semantic comparison report.
- Documentation explaining the assignment structure.

---

## Notes

This assignment is organized under the `ex02` folder so it is clearly separated from Assignment 3.

Assignment 3 is located under:

```text
ex03/
```