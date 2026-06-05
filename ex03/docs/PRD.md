# Product Requirements Document (PRD): AI Meeting Scheduler Agent

## Product Overview
The AI Meeting Scheduler Agent is a Python-based tool designed to automate the process of scheduling meetings from email requests. It monitors a dedicated Gmail account for specific labels, uses Large Language Models (LLMs) to parse natural language meeting requests, checks for availability in Google Calendar, and either schedules the event or communicates back to the requester via email.

## Background and Motivation
In a professional environment, scheduling meetings often involves back-and-forth communication to find a suitable time. This project, part of Assignment 03 in the AI Agents course, explores how autonomous agents can leverage existing APIs (Gmail and Google Calendar) and LLM capabilities to streamline administrative tasks with minimal human intervention.

## Goals
- Automate meeting scheduling from free-text emails.
- Integrate seamlessly with Gmail and Google Calendar.
- Handle missing information gracefully (e.g., defaulting duration).
- Provide feedback to the sender if a conflict exists or information is missing.

## Non-Goals
- Integration with other calendar providers (Outlook, iCal, etc.).
- Handling complex multi-person availability coordination (focus is on the agent owner's calendar).
- Building a front-end UI (CLI/Script-based execution).

## Target User
Individuals or teams who want to automate their personal or shared calendar management via a dedicated email inbox.

## System Scope
The system operates within the scope of a single Gmail account and its associated Google Calendar. It only processes emails labeled with `AI_MEETINGS` received within the last 48 hours.

## Functional Requirements
1. **Email Scanning:**
   - Connect to Gmail API using OAuth.
   - Filter for emails with the label `AI_MEETINGS`.
   - Only process emails from the last two days.
2. **Intent Extraction:**
   - Use an LLM to determine if the email is a meeting request.
   - Extract: Subject/Title, Date, Start Time, and Duration.
   - If the email is not a meeting request, the agent must take no action.
3. **Information Validation:**
   - **Mandatory:** Date and Start Time.
   - **Optional:** Duration (default to 60 minutes if missing).
   - If mandatory info is missing, send a reply email asking for details.
4. **Calendar Integration:**
   - Check Google Calendar for availability at the requested time.
   - If free: Create the calendar event.
   - If busy: Send a reply email indicating the conflict and suggesting the user pick another time.
5. **Notification:**
   - Send a confirmation email once the event is successfully scheduled.

## Non-Functional Requirements
- **Reliability:** The agent should handle API rate limits and connection errors.
- **Accuracy:** High precision in extracting dates and times from natural language.
- **Performance:** Processing an email should take less than 30 seconds.

## Security and Privacy Requirements
- **Credential Safety:** Never expose API keys, Client IDs, Client Secrets, `token.json`, or `.env` files in source control (GitHub).
- **OAuth:** Use standard OAuth2 flows for secure access to Google APIs.
- **Privacy:** Only scan emails explicitly labeled `AI_MEETINGS`.

## Edge Cases
- **Missing Date/Time:** Request clarification from the sender.
- **Ambiguous Dates:** LLM should handle "next Tuesday" or "tomorrow at 3 PM" correctly relative to the current date.
- **Overlapping Events:** Identify "busy" status in Google Calendar and notify the sender.
- **Invalid Label:** Ignore any emails without the `AI_MEETINGS` label.

## Example Input Emails and Expected Behavior
- **Scenario 1:** "Hi, can we meet tomorrow at 10 AM for a project sync?"
  - *Result:* Extracted Date (Tomorrow), Time (10:00), Duration (60m). Event created if free.
- **Scenario 2:** "Let's catch up later. Send me the notes."
  - *Result:* Not a meeting request. No action taken.
- **Scenario 3:** "Meeting on Friday morning?"
  - *Result:* Missing Start Time. Reply email sent asking for a specific time.

## Success Criteria
- Successfully parses a variety of natural language meeting requests.
- Correctly identifies availability conflicts in Google Calendar.
- Scheduled events appear accurately in the user's calendar.
- Zero credentials leaked in the repository.

## Suggested Technical Stack
- **Language:** Python 3.10+
- **APIs:** Google Gmail API, Google Calendar API.
- **Auth:** Google OAuth2 (`google-auth-oauthlib`, `google-api-python-client`).
- **LLM:** OpenAI GPT-4o or equivalent (via API).
- **Environment Management:** `python-dotenv`.

## Repository Requirements
- `.gitignore` must include `.env`, `*.json` (credentials), and `__pycache__`.
- `requirements.txt` for dependency management.
- `README.md` with setup instructions.

## Main Implementation Decision
**Direct Google APIs vs. MCP:**
While the Model Context Protocol (MCP) was discussed during the course as a standard for agent-tool communication, this project will utilize **direct Google APIs** for Gmail and Calendar.
- **Reasoning:** Direct API integration provides more granular control over the filtering logic (e.g., specific labels and date ranges), simplifies the debugging process for this specific assignment, and avoids the overhead of setting up an MCP server for a single-agent utility.
