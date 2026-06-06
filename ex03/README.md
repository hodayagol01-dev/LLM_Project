# Assignment 03: AI Meeting Scheduler Agent

## Project Overview
The **AI Meeting Scheduler Agent** is an autonomous assistant designed to streamline meeting management. It monitors a dedicated Gmail account for specific requests, uses a Large Language Model (LLM) to understand natural language meeting details, checks for availability in Google Calendar, and automatically schedules events or coordinates via email if conflicts arise.

## Assignment Context
This project is part of the **AI Agents Course (Assignment 03)**. The goal is to demonstrate the integration of LLMs with real-world APIs (Gmail and Google Calendar) to perform administrative tasks with minimal human intervention, focusing on practical tool-use and autonomous decision-making.

## Main Features
- **Automated Email Scanning:** Periodically checks for emails with the `AI_MEETINGS` label received within the last 48 hours.
- **Natural Language Understanding:** Extracts meeting titles, dates, start times, and durations from free-text emails using GPT-4o.
- **Smart Scheduling:** Checks Google Calendar for "Free/Busy" status before booking.
- **Auto-Reply Coordination:** 
  - Sends confirmation emails upon successful scheduling.
  - Notifies senders of calendar conflicts.
  - Requests missing information (date/time) if necessary.
- **Duplicate Prevention:** Tracks processed emails to ensure no request is handled twice.

## Repository Structure
```text
.
├── src/                  # Source code for the agent
│   ├── main.py           # Application entry point
│   ├── gmail_service.py  # Gmail API integration
│   ├── calendar_service.py # Google Calendar integration
│   └── llm_parser.py     # LLM logic and prompts
├── tests/                # Unit and integration tests
├── docs/                 # Project documentation
│   ├── PRD.md            # Product Requirements Document
│   ├── PLAN.md           # Technical Implementation Plan
│   └── TODO.md           # Implementation Checklist
├── .env.example          # Template for environment variables
├── .gitignore            # Git exclusion rules
└── requirements.txt      # Project dependencies
```

## Technologies Used
- **Language:** Python 3.10+
- **LLM:** OpenAI GPT-4o (via API)
- **Google APIs:** Gmail API, Google Calendar API
- **Auth:** Google OAuth 2.0 (`google-auth-oauthlib`)
- **Environment:** `python-dotenv`

## 🛡️ Security Note
**Critical:** This project interacts with sensitive Google and OpenAI credentials. 
- Never commit `.env` files.
- Never commit `credentials.json` (GCP Client Secrets).
- Never commit `token.json` (User OAuth tokens).
- Ensure `.gitignore` is properly configured before pushing any changes.

## How It Works
1. **Fetch:** The agent scans the Gmail inbox for the label `AI_MEETINGS`.
2. **Analyze:** The LLM parses the email body to identify the intent and extract structured meeting data.
3. **Validate:** The agent checks if the required date and time are present; if not, it replies asking for details.
4. **Check:** It queries Google Calendar for the requested slot.
5. **Action:**
   - If **Free**: Creates the calendar event and sends a confirmation email.
   - If **Busy**: Sends an email suggesting the user pick another time.

## Documentation
For more detailed information, please refer to:
- [Product Requirements Document (PRD)](docs/PRD.md)
- [Implementation Plan](docs/PLAN.md)
- [TODO Checklist](docs/TODO.md)

## Project Status

Current Phase: Google Workspace API Integration Completed.

The AI Meeting Scheduler Agent has been integrated with real Google Workspace APIs:
  * Real Google OAuth authentication using `auth_test.py`.
  * Real Gmail API integration for reading inbox emails.
  * Real Gmail API integration for sending reply emails.
  * Real Gmail API integration for marking emails as processed/read.
  * Real Google Calendar API integration for checking calendar availability.
  * Real Google Calendar API integration for creating calendar events.
  * Local `credentials.json` and `token.json` files are required for running the project locally, but they are intentionally ignored by Git for security.

The project also includes integration test files:
  * `auth_test.py`
  * `gmail_read_test.py`
  * `calendar_create_test.py`


## MCP Architecture

This project now includes a dual Model Context Protocol (MCP) architecture in addition to the original direct implementation.

The MCP architecture includes two parts:

- `src/mcp_server.py` — MCP Server that exposes the project capabilities as tools.
- `src/agent.py` — MCP Client Agent that connects to the server, discovers the tools, and runs the scheduling workflow.

The MCP Server exposes tools for:

- Fetching recent Gmail emails.
- Parsing meeting requests.
- Checking Google Calendar availability.
- Creating Google Calendar events.
- Sending reply emails.
- Marking emails as processed.

The MCP Client Agent runs an autonomous workflow:

1. Fetch recent emails.
2. Parse each email as a possible meeting request.
3. Ask for clarification if required details are missing.
4. Check calendar availability.
5. Create a calendar event if the time slot is free.
6. Send a confirmation or busy reply.
7. Mark the email as processed.

This separates tool execution from agent decision-making, following the MCP client/server architecture discussed in the course.

## How to Run

1. Create a Google Cloud project.
2. Enable Gmail API and Google Calendar API.
3. Create OAuth Desktop credentials.
4. Download `credentials.json` into the `ex03` project root.
5. Run `python3 auth_test.py` to create `token.json`.
6. Run `python3 main.py`.

## Security Note

Do not commit `credentials.json`, `token.json`, `.env`, API keys, client secrets, or tokens to GitHub.
These files are required only for local execution and are ignored by `.gitignore`.

### MCP Client/Server Run

The project also includes an MCP-based implementation.

To run it, use the Python virtual environment created for this project:

```bash
source .venv/bin/activate
python -m src.agent
```

In this mode, `src/agent.py` runs as the MCP Client Agent and connects to `src/mcp_server.py`, which exposes the Gmail, Calendar, and parsing tools.
