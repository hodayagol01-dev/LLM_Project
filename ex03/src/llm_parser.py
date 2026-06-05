"""
LLM-style email parser for the AI Meeting Scheduler Agent.

This module is responsible for understanding whether an email is a meeting
request and extracting structured meeting details from free text.

For this academic implementation, the parser combines deterministic rules
with clear TODO points for replacing the logic with a real LLM provider.
This keeps the agent runnable while still demonstrating the intended
LLM-based architecture.
"""

import re
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


TIMEZONE = "Asia/Jerusalem"


MEETING_KEYWORDS = [
    "meet",
    "meeting",
    "schedule",
    "call",
    "zoom",
    "appointment",
    "discuss",
    "פגישה",
    "להיפגש",
    "זום",
    "שיחה",
]


NON_MEETING_HINTS = [
    "lunch",
    "newsletter",
    "promotion",
    "sale",
    "receipt",
    "invoice",
]


def is_meeting_request(email_text):
    """
    Determine whether an email looks like a meeting request.

    Args:
        email_text: Email subject/body/snippet text.

    Returns:
        True if the email appears to request a meeting, otherwise False.
    """
    text = (email_text or "").lower()

    if any(hint in text for hint in NON_MEETING_HINTS):
        return False

    return any(keyword in text for keyword in MEETING_KEYWORDS)


def _extract_time(text):
    """
    Extract a time such as 10:00, 10am, 10 AM, or 14:30.

    Returns:
        A tuple of (hour, minute), or None if no time was found.
    """
    if not text:
        return None

    text = text.lower()

    # Matches 10:00, 14:30
    match = re.search(r"\b([01]?\d|2[0-3]):([0-5]\d)\b", text)
    if match:
        return int(match.group(1)), int(match.group(2))

    # Matches 10am, 10 AM, 2pm
    match = re.search(r"\b(1[0-2]|0?[1-9])\s*(am|pm)\b", text)
    if match:
        hour = int(match.group(1))
        suffix = match.group(2)
        if suffix == "pm" and hour != 12:
            hour += 12
        if suffix == "am" and hour == 12:
            hour = 0
        return hour, 0

    return None


def _extract_date(text):
    """
    Extract a meeting date from common free-text expressions.

    Supports:
    - tomorrow
    - today
    - explicit YYYY-MM-DD date
    - simple weekday names

    Returns:
        A date object.
    """
    tz = ZoneInfo(TIMEZONE)
    now = datetime.now(tz)
    lower_text = (text or "").lower()

    if "tomorrow" in lower_text or "מחר" in lower_text:
        return (now + timedelta(days=1)).date()

    if "today" in lower_text or "היום" in lower_text:
        return now.date()

    explicit = re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", lower_text)
    if explicit:
        return datetime.fromisoformat(explicit.group(1)).date()

    weekdays = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "sunday": 6,
        "יום שני": 0,
        "יום שלישי": 1,
        "יום רביעי": 2,
        "יום חמישי": 3,
        "יום שישי": 4,
        "יום ראשון": 6,
    }

    for name, target_weekday in weekdays.items():
        if name in lower_text:
            days_ahead = (target_weekday - now.weekday()) % 7
            if days_ahead == 0:
                days_ahead = 7
            return (now + timedelta(days=days_ahead)).date()

    return None


def _extract_location(text):
    """
    Extract a simple meeting location from free text.

    Returns:
        A location string.
    """
    lower_text = (text or "").lower()

    if "zoom" in lower_text:
        return "Zoom"
    if "google meet" in lower_text:
        return "Google Meet"
    if "teams" in lower_text:
        return "Microsoft Teams"
    if "bar-ilan" in lower_text or "bar ilan" in lower_text:
        return "Bar-Ilan University"

    return ""


def extract_meeting_details(email):
    """
    Extract structured meeting details from an email dictionary or raw text.

    Args:
        email: Dictionary containing subject/sender/body/snippet, or a raw string.

    Returns:
        Dictionary with extracted meeting details.
    """
    if isinstance(email, str):
        subject = "Meeting request"
        body = email
        sender = ""
    else:
        subject = email.get("subject", "")
        body = email.get("body", "") or email.get("snippet", "")
        sender = email.get("sender", "")

    combined_text = f"{subject}\n{body}"

    meeting_detected = is_meeting_request(combined_text)

    if not meeting_detected:
        return {
            "is_meeting_request": False,
            "missing_fields": [],
        }

    extracted_date = _extract_date(combined_text)
    extracted_time = _extract_time(combined_text)
    location = _extract_location(combined_text)

    missing_fields = []
    if extracted_date is None:
        missing_fields.append("date")
    if extracted_time is None:
        missing_fields.append("start_time")

    start_time = None
    end_time = None

    if extracted_date is not None and extracted_time is not None:
        hour, minute = extracted_time
        tz = ZoneInfo(TIMEZONE)
        start_dt = datetime(
            extracted_date.year,
            extracted_date.month,
            extracted_date.day,
            hour,
            minute,
            tzinfo=tz,
        )
        end_dt = start_dt + timedelta(minutes=60)

        start_time = start_dt.isoformat()
        end_time = end_dt.isoformat()

    return {
        "is_meeting_request": True,
        "title": subject or "Meeting request",
        "start_time": start_time,
        "end_time": end_time,
        "location": location,
        "participants": [sender] if sender else [],
        "sender": sender,
        "missing_fields": missing_fields,
        "raw_text": combined_text,
    }


def parse_email(email):
    """
    Backward-compatible wrapper for the meeting agent.

    This function keeps the agent code simple while allowing the parser
    implementation to improve over time.
    """
    return extract_meeting_details(email)
