# Token and Cost Report - Assignment 06

## Project

Assignment 06 - Multimedia Vibe Coding  
Project name: ShoreStep AI  
Output: Remotion-based 60-second multimedia video

## Purpose of This Report

This report documents the estimated AI usage, prompt iterations, and cost considerations for the multimedia generation workflow.

The project was developed through a Vibe Coding process: human intent was translated into structured prompts, documentation, script files, scene JSON, Remotion code, QA checks, and a rendered multimedia output.

## Tools Used

| Tool / Model | Purpose | Cost Type |
|---|---|---|
| ChatGPT | Planning, documentation, storyboard refinement, QA thinking | Subscription-based usage |
| Gemini CLI | Code generation and Remotion project assistance | API / account-based usage |
| Remotion | Programmatic video rendering | Local execution |
| GitHub | Version control and submission | Free repository hosting |
| Local terminal | Build, render, and verification | No token cost |

## Main Prompt Categories

| Category | Description | Estimated Usage |
|---|---|---|
| Planning prompts | PRD, PLAN, TODO, project scope and requirements | Medium |
| Story prompts | Script, scene structure, emotional arc, visual direction | Medium |
| Code prompts | Remotion setup, component structure, rendering fixes | High |
| QA prompts | Build verification, playback troubleshooting, documentation review | Medium |
| Refinement prompts | Flow improvement, storyboard polish, final checks | Medium |

## Estimated Token Usage

The exact token count was not exported from all tools, so the following is a reasonable estimate based on the number and size of prompt iterations:

| Stage | Estimated Tokens |
|---|---:|
| Requirements and planning | 8,000 - 12,000 |
| Script and scene planning | 6,000 - 10,000 |
| Remotion code generation and debugging | 18,000 - 30,000 |
| QA and documentation review | 8,000 - 14,000 |
| Final refinement and GitHub readiness | 6,000 - 10,000 |

Estimated total usage: **46,000 - 76,000 tokens**

## Estimated Direct Cost

No paid per-call OpenAI API billing was used for this assignment.

The work was completed using subscription/account-based AI tools and local rendering. Therefore, the direct incremental cost for this specific assignment is estimated as:

**$0.00 direct API cost**

If the same workflow were executed through paid API calls only, the cost would depend on the exact model and token pricing. For this submission, the relevant cost consideration is the estimated token usage and tool workflow rather than direct API billing.

## Cost Control Measures

- Reused a stable Remotion structure instead of regenerating the project repeatedly.
- Replaced local video playback with extracted still frames to avoid repeated render failures.
- Performed final rendering locally with Remotion.
- Limited late-stage changes to focused manual edits instead of broad AI rewrites.
- Used Git commits to preserve stable versions and avoid losing working states.

## Final Assessment

The project demonstrates controlled AI-assisted multimedia development with a reasonable token footprint. Most AI usage was concentrated in code generation, debugging, and storyboard refinement. The final rendered output was produced locally and committed to GitHub.
