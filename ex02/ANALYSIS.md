# Assignment 2 – Research and Analysis

## Purpose

This document explains the research and analysis process behind Assignment 2.

The goal of the assignment is to build a multi-agent translation chain and evaluate how much meaning is preserved after a sentence passes through several translation steps.

The translation chain is:

```text
English → French → Hebrew → English
```

The final English sentence is compared to the original English sentence in order to evaluate semantic preservation.

---

## Research Question

The main research question was:

How much of the original meaning is preserved after a sentence passes through a multi-agent translation chain?

This question connects to the course topics of:

- Prompt engineering
- Skills
- Agents
- Tokens
- Vectors
- Semantic similarity
- Meaning preservation

---

## Agentic Design

The project was designed as a small multi-agent workflow.

Each step has a dedicated role:

1. Agent 1 translates from English to French.
2. Agent 2 translates from French to Hebrew.
3. Agent 3 translates from Hebrew back to English.
4. The comparison step evaluates the semantic similarity between the original and final English sentences.

This design follows the idea that each agent can use a different specialized skill.

---

## Skills Used

The project includes separate skill-style Markdown files:

| Skill File | Purpose |
|---|---|
| `agent1_french_skill.md` | English to French translation |
| `agent2_hebrew_skill.md` | French to Hebrew translation |
| `agent3_english_skill.md` | Hebrew to English translation |
| `comparison_skill.md` | Semantic comparison between the original and final English sentences |

The purpose of separating the skills is to keep each role focused and clear.

---

## Orchestrator

The file `orchestrator_agent.py` manages the full workflow.

The orchestrator reads the original sentence, runs the translation chain, performs the comparison, and saves the final report.

The workflow is:

```text
source_english.txt
→ agent1_french.txt
→ agent2_hebrew.txt
→ agent3_english.txt
→ comparison_report.txt
```

This makes the solution more agentic because the process is managed as one coordinated pipeline instead of unrelated manual steps.

---

## Semantic Comparison

The comparison stage evaluates whether the final English sentence is semantically close to the original sentence.

The current implementation uses a simple vector-based comparison approach.

It compares the original English sentence and the final English sentence and produces:

- Semantic similarity
- Semantic distance
- A short comparison report

In the current tested run, the result was:

```text
Semantic similarity: 1.0000
Semantic distance: 0.0000
```

This means that for the tested sentence, the final English output preserved the meaning of the original sentence.

---

## Example Tested Sentence

Original sentence:

```text
One for all and all for one
```

Translation chain:

```text
English → French → Hebrew → English
```

Final English output:

```text
One for all and all for one
```

In this case, the meaning was preserved successfully.

---

## Why Semantic Comparison Matters

A literal word-by-word comparison is not enough for translation quality.

A translated sentence may use different words but still preserve the same meaning.

Therefore, the comparison step focuses on semantic similarity rather than exact wording only.

This is connected to the course concepts of vectors and semantic distance.

---

## Observations

During the implementation, we observed that:

1. A translation chain can preserve meaning when the sentence is simple and clear.
2. Each translation step may introduce small wording changes.
3. The final comparison step is important because it gives an analytical layer to the project.
4. The orchestrator improves the structure because it connects all steps into one workflow.
5. Skill files make the agent roles easier to understand and maintain.

---

## Limitations

The current implementation demonstrates the required concept, but it has some limitations:

1. The semantic comparison is a basic vector-based comparison.
2. The project currently uses one main test sentence.
3. The translation chain includes only three language transitions.
4. More sentences should be tested in order to evaluate robustness.
5. A future version could use model-generated embeddings and cosine similarity for a stronger semantic metric.

---

## Future Improvements

Possible improvements include:

1. Add more test sentences.
2. Add automatic embedding generation.
3. Calculate cosine similarity using embedding vectors.
4. Compare several language chains.
5. Add a table of semantic similarity scores.
6. Extend the orchestrator to run multiple experiments automatically.
7. Save all experiment results in a structured report.

---

## Conclusion

Assignment 2 demonstrates a multi-agent translation workflow using specialized skills and an orchestrator.

The project shows how a sentence can move through several translation agents and then be evaluated using a semantic comparison step.

The main value of the project is not only the translation itself, but the analysis of how meaning is preserved across the chain.