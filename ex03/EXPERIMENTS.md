# Experiments and Prompt Engineering

## Purpose

This document summarizes the experimentation and prompt-engineering process behind the AI Meeting Scheduler Agent.

The goal of the project is to build an autonomous agent that can read Gmail messages, identify meeting requests, extract the relevant scheduling details, check Google Calendar availability, create calendar events when possible, and reply to the sender.

This document was added to explain the engineering reasoning behind the final implementation, not only the final code.

The experiments focused on three main questions:

1. How can the agent reliably identify whether an email is a meeting request?
2. How can the agent extract useful meeting details from imperfect natural language?
3. How should the agent behave when required information is missing or when the calendar is unavailable?

---

## Experiment 1: Basic Keyword-Based Detection

### Goal

Detect meeting requests using simple keywords such as:

- meeting
- schedule
- sync
- call
- discussion

### Example Input

```text
Hi, can we schedule a meeting about the project sync?
```

### Expected Output

```text
Meeting request detected.
```

### Result

This approach worked for simple cases, but it was too limited.

### Limitation

Some real meeting requests do not use the exact expected keywords. Other emails may contain words like "meeting" but are not actual scheduling requests.

For example:

```text
The meeting notes from yesterday are attached.
```

This email contains the word "meeting", but it is not a request to schedule a new meeting.

### Insight

Keyword detection can be useful as a fallback, but it is not reliable enough for an autonomous scheduling agent.

---

## Experiment 2: Zero-Shot Prompting

### Goal

Test whether the model can extract meeting details from an email using a general natural-language instruction.

### Prompt Strategy

The model was asked to read the email and decide whether it includes a meeting request.

### Example Input

```text
Hi, let's meet tomorrow afternoon to discuss the assignment.
```

### Observed Issue

The model could usually understand that the email was a meeting request, but it sometimes returned incomplete or inconsistent structured data.

Typical issues included:

- Missing exact time.
- Returning free text instead of JSON.
- Confusing vague time expressions such as "tomorrow afternoon".
- Guessing missing details too aggressively.

### Insight

Zero-shot prompting was not structured enough for this task. The agent needs predictable output because later steps depend on fields such as date, start time, and end time.

---

## Experiment 3: Structured JSON Schema Prompting

### Goal

Improve consistency by asking the model to return a structured JSON object.

### Improved Output Format

The parser was expected to produce fields such as:

```json
{
  "is_meeting_request": true,
  "title": "Project Sync",
  "date": "tomorrow",
  "start_time": "10:00",
  "end_time": null,
  "missing_fields": ["end_time"]
}
```

### Result

Using an explicit schema improved the reliability of the parsing step.

Instead of returning free text, the model was guided toward a predictable structure that the agent could use in the next workflow steps.

### Insight

For agentic workflows, structured output is more important than natural-sounding output. The agent needs machine-readable fields in order to decide what action to take next.

---

## Experiment 4: Handling Missing Information

### Goal

Make the agent robust when an email is clearly a meeting request but does not include all required scheduling details.

### Example Input

```text
Can we meet to discuss the project?
```

### Agent Decision

```text
The email is a meeting request, but the date and time are missing.
```

### Agent Response

```text
Hi,

Thank you for your message. I can help schedule this meeting, but I am missing some details.

Missing details: date, start_time, end_time

Please send the missing information and I will continue the scheduling process.

Best,
AI Meeting Scheduler Agent
```

### Result

This behavior made the system safer and more reliable.

### Insight

The agent should not guess important scheduling details. Asking for clarification is better than creating an incorrect calendar event.

---

## Experiment 5: Calendar Availability Check

### Goal

Check whether the requested meeting time is available before creating a calendar event.

### Scenario A: Calendar Available

Expected behavior:

1. Create a calendar event.
2. Send a confirmation email.
3. Mark the original email as processed.

### Scenario B: Calendar Busy

Expected behavior:

1. Do not create a calendar event.
2. Send a polite busy reply.
3. Ask the sender to suggest another time.
4. Mark the original email as processed.

### Insight

Calendar availability must be checked before event creation to avoid double-booking.

---

## Experiment 6: MCP Client/Server Architecture

### Goal

Upgrade the project architecture to follow a Model Context Protocol client/server design.

### Previous Approach

The original implementation called Gmail, Calendar, and parsing functions directly from the main workflow.

### Improved MCP Approach

The upgraded implementation separates the system into:

- `src/mcp_server.py` — exposes Gmail, Calendar, parsing, reply, and processing capabilities as MCP tools.
- `src/agent.py` — runs as an MCP Client Agent that discovers and calls the server tools.

### MCP Tools

The MCP Server exposes the following tools:

- `fetch_recent_emails_tool`
- `parse_meeting_request_tool`
- `check_calendar_availability_tool`
- `create_calendar_event_tool`
- `send_reply_email_tool`
- `mark_email_as_processed_tool`

### Result

The MCP architecture makes the project more modular and closer to a professional agent-tool system.

### Insight

Using MCP improves separation of concerns:

- The server owns the tools.
- The client owns the workflow.
- The agent can discover and invoke tools dynamically.
- The system is easier to extend and maintain.

---

## Simulated Test Scenarios

The following scenarios were used to validate the agent behavior:

| Scenario | Input Type | Expected Behavior | Result |
|---|---|---|---|
| Non-meeting email | General email with no scheduling request | Ignore or skip | Passed |
| Meeting request with missing details | Email asks to meet but does not include full time details | Send clarification email | Passed |
| Complete meeting request | Email includes meeting topic and time | Check calendar availability | Passed |
| Calendar available | Requested time slot is free | Create event and send confirmation | Passed |
| Calendar busy | Requested time slot is already occupied | Do not create event and ask for another time | Passed |

---

## Final Agent Workflow

The final workflow is:

1. Fetch recent Gmail emails.
2. Detect whether each email is a meeting request.
3. Extract meeting details.
4. If details are missing, send a clarification email.
5. If details are complete, check calendar availability.
6. If the time slot is available, create a calendar event.
7. If the time slot is busy, send a busy reply.
8. Mark the email as processed.

---

## Key Lessons Learned

1. Natural language emails are often incomplete or ambiguous.
2. A responsible scheduling agent should avoid guessing important details.
3. Structured JSON output makes the workflow more reliable.
4. Clarification messages improve the user experience.
5. Calendar availability checks are necessary before creating events.
6. MCP improves the architecture by separating tools from agent logic.
7. Documentation of experiments is important because it explains the engineering decisions behind the final implementation.

---

## Current Limitations

The current system is functional, but it still has limitations:

1. Parsing vague natural language expressions such as "next Monday morning" can be improved.
2. The system currently focuses on Gmail and Google Calendar.
3. The user experience is demonstrated mainly through logs and documentation rather than a graphical interface.
4. More automated tests could be added for additional edge cases.
5. Recurring meetings are not fully supported yet.

---

## Future Improvements

Possible future improvements include:

1. Stronger LLM-based parsing for complex scheduling requests.
2. More robust timezone handling.
3. More automated tests.
4. Support for multiple calendars.
5. A clearer user-facing dashboard or CLI summary.
6. Better handling of recurring meetings.
7. More detailed logging for debugging and evaluation.