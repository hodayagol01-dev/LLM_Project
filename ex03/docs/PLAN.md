# Implementation Plan: AI Meeting Scheduler Agent

This document outlines the step-by-step plan for building the AI Meeting Scheduler Agent.

## 1. Repository Setup
- [ ] Initialize a new Git repository.
- [ ] Create the project structure:
  ```text
  .
  ├── src/
  │   ├── main.py            # Entry point
  │   ├── gmail_service.py   # Gmail API logic
  │   ├── calendar_service.py # Google Calendar API logic
  │   ├── llm_parser.py      # LLM integration and prompt engineering
  │   └── utils.py           # Helper functions
  ├── tests/                 # Unit and integration tests
  ├── docs/                  # PRD, PLAN, etc.
  ├── .env                   # Sensitive keys (ignored)
  ├── .env.example           # Template for environment variables
  ├── .gitignore             # Git ignore rules
  └── requirements.txt       # Dependencies
  ```
- [ ] Set up a Python virtual environment (`python -m venv venv`).
- [ ] Initialize `.gitignore` to exclude `.env`, `token.json`, `credentials.json`, `__pycache__`, and `venv/`.

## 2. Google Account and API Setup
- [ ] Create a dedicated Google Cloud Project.
- [ ] Enable the **Gmail API** and **Google Calendar API**.
- [ ] Configure the **OAuth Consent Screen** (Internal/Testing mode).
- [ ] Create **OAuth 2.0 Client IDs** (Desktop application).
- [ ] Download `credentials.json` and place it in the project root (temporarily for auth setup).

## 3. Authentication and Security Setup
- [ ] Implement a reusable authentication module using `google-auth-oauthlib`.
- [ ] Define scopes:
  - `https://www.googleapis.com/auth/gmail.modify` (to read and label emails)
  - `https://www.googleapis.com/auth/calendar` (to read and write events)
- [ ] Create a script to generate and refresh `token.json`.
- [ ] Configure `.env.example` with placeholders for:
  - `OPENAI_API_KEY`
  - `GMAIL_USER_EMAIL`
  - `CALENDAR_ID` (default to 'primary')

## 4. Gmail Scanning Logic
- [ ] Implement `list_messages` with a query filter:
  - `label:AI_MEETINGS`
  - `newer_than:2d`
- [ ] Fetch full message content for each message ID found.
- [ ] Extract relevant fields: `From`, `Subject`, `Date`, and the `Body` (plain text).

## 5. LLM Parsing Logic
- [ ] Integrate an LLM provider (e.g., OpenAI GPT-4o).
- [ ] Design a system prompt to:
  - Identify if the email is a meeting request.
  - Extract: `title`, `date`, `start_time`, `duration` (minutes).
  - Handle relative dates (e.g., "next Monday") by providing the "current date/time" in the prompt.
- [ ] Enforce structured output (JSON format) from the LLM.
- [ ] Implement fallback logic for missing duration (default to 60 mins).

## 6. Calendar Availability Check
- [ ] Parse LLM-extracted date/time into Python `datetime` objects.
- [ ] Define the meeting time range (start to end).
- [ ] Use `service.events().list()` or `service.freebusy().query()` to check for overlapping events in the user's primary calendar.

## 7. Calendar Event Creation
- [ ] If the slot is free, construct an event resource:
  - `summary`: Extracted title.
  - `start`: ISO format datetime.
  - `end`: ISO format datetime.
  - `attendees`: Include the sender's email.
- [ ] Call `service.events().insert()` to create the event.

## 8. Reply Email Logic
- [ ] Create three response templates:
  - **Success:** Confirming the meeting date, time, and link.
  - **Conflict:** Notifying that the slot is busy and suggesting alternatives.
  - **Clarification:** Asking for missing mandatory info (Date or Start Time).
- [ ] Implement `send_reply` using Gmail API, ensuring the reply is threaded (using `ThreadId` and `In-Reply-To` headers).

## 9. Duplicate Processing Prevention
- [ ] Implement a tracking mechanism to avoid processing the same email multiple times.
- [ ] Options:
  - Use a local `processed_emails.json` file to store Message IDs.
  - Add a sub-label (e.g., `AI_MEETINGS/PROCESSED`) or remove the `AI_MEETINGS` label after processing. (Preferred: Use a local log for simplicity in this assignment).

## 10. Testing Plan
- [ ] **Unit Tests:** Mock LLM responses with various email inputs (valid, missing info, non-meeting).
- [ ] **Integration Tests:** Use a test Gmail account to verify scanning and labeling logic.
- [ ] **End-to-End Test:** Send a real email, verify LLM parsing, check Calendar for the event, and confirm receipt of the reply email.

## 11. Documentation Plan
- [ ] **README.md:** Clear setup instructions (Google Cloud steps, environment variables, running the agent).
- [ ] **Code Documentation:** Docstrings for all major functions and classes.
- [ ] **Architecture Diagram:** Simple flow showing Email -> LLM -> Calendar -> Reply.

## 12. GitHub Submission Checklist
- [ ] [ ] Verify `.gitignore` is correctly configured (no secrets!).
- [ ] [ ] Ensure `requirements.txt` is up to date.
- [ ] [ ] Check that `src/main.py` is executable and documented.
- [ ] [ ] Provide a sample `.env.example`.
- [ ] [ ] Perform a final "clean repo" check.
