"""
Google Calendar service for the AI Meeting Scheduler Agent.

This module uses the real Google Calendar API through OAuth.
It expects token.json to exist locally and to be ignored by Git.
"""

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


TOKEN_FILE = "token.json"
TIMEZONE = "Asia/Jerusalem"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/calendar",
]


def get_calendar_service():
    """
    Authenticate with Google Calendar using the local token.json file.

    Returns:
        Google Calendar API service object, or None if authentication fails.
    """
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        return build("calendar", "v3", credentials=creds)
    except Exception as error:
        print(f"ERROR: Failed to obtain calendar service: {error}")
        return None


def _normalize_datetime(value):
    """
    Convert a date/time value into a valid RFC3339 datetime string.

    If the incoming value is invalid or incomplete, fall back to tomorrow at 10:00.
    This keeps the academic demo stable even when the LLM extracts a partial date.
    """
    tz = ZoneInfo(TIMEZONE)

    if isinstance(value, datetime):
        dt = value
    else:
        try:
            text = str(value).strip()

            # Fix common malformed format, for example: 2026-06T10:00:00
            if len(text) >= 16 and text[4] == "-" and "T" in text:
                date_part, time_part = text.split("T", 1)
                if date_part.count("-") == 1:
                    tomorrow = datetime.now(tz) + timedelta(days=1)
                    text = f"{tomorrow.date().isoformat()}T{time_part}"

            dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
        except Exception:
            dt = datetime.now(tz) + timedelta(days=1)
            dt = dt.replace(hour=10, minute=0, second=0, microsecond=0)

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=tz)

    return dt.isoformat()



def _normalize_time_range(start_time, end_time):
    """
    Normalize start and end times and ensure the range is not empty.
    If end_time is missing, invalid, or not after start_time, default to 30 minutes.
    """
    tz = ZoneInfo(TIMEZONE)

    start_iso = _normalize_datetime(start_time)
    end_iso = _normalize_datetime(end_time)

    start_dt = datetime.fromisoformat(start_iso)
    end_dt = datetime.fromisoformat(end_iso)

    if end_dt <= start_dt:
        end_dt = start_dt + timedelta(minutes=30)

    if start_dt.tzinfo is None:
        start_dt = start_dt.replace(tzinfo=tz)
    if end_dt.tzinfo is None:
        end_dt = end_dt.replace(tzinfo=tz)

    return start_dt.isoformat(), end_dt.isoformat()


def check_availability(start_time, end_time):
    """
    Check whether the primary calendar is free for the requested time slot.

    Args:
        start_time: Requested meeting start time.
        end_time: Requested meeting end time.

    Returns:
        True if the calendar is free, False if busy or if an API error occurs.
    """
    service = get_calendar_service()
    if not service:
        return False

    start_iso, end_iso = _normalize_time_range(start_time, end_time)

    body = {
        "timeMin": start_iso,
        "timeMax": end_iso,
        "timeZone": TIMEZONE,
        "items": [{"id": "primary"}],
    }

    try:
        result = service.freebusy().query(body=body).execute()
        busy_slots = result.get("calendars", {}).get("primary", {}).get("busy", [])
        is_free = len(busy_slots) == 0

        if is_free:
            print("DEBUG: Calendar is free for the requested time.")
        else:
            print("DEBUG: Calendar is busy for the requested time.")

        return is_free

    except HttpError as error:
        print(f"ERROR: An API error occurred while checking availability: {error}")
        return False
    except Exception as error:
        print(f"ERROR: An unexpected error occurred while checking availability: {error}")
        return False


def create_calendar_event(title, start_time, end_time, description="", location=""):
    """
    Create a new event in the user's primary Google Calendar.

    Args:
        title: Event title.
        start_time: Event start time.
        end_time: Event end time.
        description: Optional event description.
        location: Optional event location.

    Returns:
        The created event dictionary, or None if creation fails.
    """
    service = get_calendar_service()
    if not service:
        return None

    start_iso, end_iso = _normalize_time_range(start_time, end_time)

    event = {
        "summary": title,
        "location": location,
        "description": description,
        "start": {
            "dateTime": start_iso,
            "timeZone": TIMEZONE,
        },
        "end": {
            "dateTime": end_iso,
            "timeZone": TIMEZONE,
        },
    }

    try:
        created_event = service.events().insert(
            calendarId="primary",
            body=event,
        ).execute()

        print(f"DEBUG: Event '{title}' created successfully. Link: {created_event.get('htmlLink')}")
        return created_event

    except HttpError as error:
        print(f"ERROR: An API error occurred while creating event: {error}")
        return None
    except Exception as error:
        print(f"ERROR: An unexpected error occurred while creating event: {error}")
        return None
