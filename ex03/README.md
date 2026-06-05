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
**Current Phase:** Initial Development and Setup (using placeholder logic).
- [x] Product Requirements Document (PRD) defined.
- [x] Technical Implementation Plan (PLAN) defined.
- [x] TODO checklist exists.
- [x] README.md exists and is being maintained.
- [x] Initial Python project skeleton (`src/`, `tests/`) is established.
- [x] Placeholder agent flow runs successfully via `python3 main.py`.
- [ ] Real Google API (Gmail, Calendar) integration is not yet implemented.
**Important Note:** This project currently utilizes placeholder/demo logic for its core functionalities and does NOT perform actual Gmail or Calendar API calls. All interactions are simulated for development and testing purposes.
