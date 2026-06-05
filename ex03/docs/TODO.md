# AI Meeting Scheduler Agent - TODO Checklist

## 1. Project Initialization & Documentation
- [ ] Initialize Git repository.
- [ ] Create folder structure (`src/`, `tests/`, `docs/`).
- [ ] Ensure `docs/PRD.md` is complete.
- [ ] Ensure `docs/PLAN.md` is complete.
- [ ] Create `README.md` with project overview and setup instructions.

## 2. Google Account & Workspace Setup
- [ ] Access/Create a dedicated Gmail account for the agent.
- [ ] Manually create the `AI_MEETINGS` label in the Gmail account.
- [ ] Send a few test emails to the account and apply the `AI_MEETINGS` label.

## 3. Google Cloud Platform (GCP) Configuration
- [ ] Create a new GCP Project (e.g., `ai-meeting-scheduler`).
- [ ] Enable **Gmail API**.
- [ ] Enable **Google Calendar API**.
- [ ] Configure **OAuth Consent Screen** (User Type: External, Status: Testing).
- [ ] Add the agent's Gmail account as a Test User.
- [ ] Create **OAuth 2.0 Client ID** (Application Type: Desktop App).
- [ ] Download `credentials.json` and save to project root (DO NOT COMMIT).

## 4. Environment & Security
- [ ] Create `.gitignore` to exclude:
    - `.env`
    - `credentials.json`
    - `token.json`
    - `__pycache__/`
    - `venv/`
    - `.pytest_cache/`
- [ ] Create `.env.example` with required keys:
    - `OPENAI_API_KEY`
    - `GMAIL_USER_EMAIL`
- [ ] Create a virtual environment and install dependencies:
    - `google-api-python-client`
    - `google-auth-oauthlib`
    - `openai`
    - `python-dotenv`

## 5. Core Implementation
- [ ] **Authentication Module:** Implement OAuth2 flow to generate `token.json`.
- [ ] **Gmail Service:**
    - [ ] Implement scanning for emails with `AI_MEETINGS` label from the last 2 days.
    - [ ] Extract email body, sender, and timestamp.
- [ ] **LLM Integration:**
    - [ ] Set up OpenAI client.
    - [ ] Craft system prompt for structured JSON extraction (Title, Date, Start Time, Duration).
    - [ ] Handle relative date parsing (passing "today's date" to the LLM).
- [ ] **Calendar Service:**
    - [ ] Implement availability check (free/busy) for the requested slot.
    - [ ] Implement event creation logic.
- [ ] **Email Responder:**
    - [ ] Implement threaded reply logic.
    - [ ] Create templates for Success, Busy, and Missing Info scenarios.
- [ ] **Main Orchestrator:**
    - [ ] Connect all services in `main.py`.
    - [ ] Implement a mechanism to avoid re-processing emails (e.g., `processed_emails.log`).

## 6. Testing & Validation
- [ ] **Test Case: Successful Scheduling**
    - Email with clear date/time.
    - Calendar is free.
    - Result: Event created + Confirmation email.
- [ ] **Test Case: Non-Meeting Email**
    - Email with label but unrelated content.
    - Result: No action taken.
- [ ] **Test Case: Missing Details**
    - Email missing time or date.
    - Result: Reply email sent asking for details.
- [ ] **Test Case: Calendar Conflict**
    - Requested time overlaps with existing event.
    - Result: Reply email sent informing about the conflict.
- [ ] **Test Case: Duration Defaulting**
    - Email with date/time but no duration.
    - Result: Event created with 60-minute default.

## 7. Finalization & Submission
- [ ] Conduct a final code review for cleanliness and comments.
- [ ] Verify no secrets or `token.json`/`credentials.json` are in the Git history.
- [ ] Update `requirements.txt` (`pip freeze > requirements.txt`).
- [ ] Final check of `README.md` for clarity.
- [ ] Submit the repository URL.
