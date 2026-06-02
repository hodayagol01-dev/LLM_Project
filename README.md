# LLM Multi-Agent Translation Chain

This project demonstrates a multi-agent LLM workflow.

The system starts with an English sentence, passes it through three translation agents, and then compares the final English sentence to the original sentence.

## Workflow

1. Agent 1: English to French
2. Agent 2: French to Hebrew
3. Agent 3: Hebrew to English
4. Comparison Tool: compares the original English sentence with the final English sentence

## Input

source_english.txt

## Outputs

agent1_french.txt  
agent2_hebrew.txt  
agent3_english.txt  
comparison_report.txt

## Result

Original sentence:
One for all and all for one

Final sentence:
One for all and all for one

Semantic Distance:
0

## Course Concepts

This project demonstrates:
- AI agents
- Skills
- Orchestration
- Multi-step LLM workflow
- Semantic comparison
