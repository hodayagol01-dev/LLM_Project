from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/calendar",
]

TOKEN_FILE = "token.json"
TIMEZONE = "Asia/Jerusalem"


def main():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    service = build("calendar", "v3", credentials=creds)

    start = datetime.now(ZoneInfo(TIMEZONE)) + timedelta(days=1)
    start = start.replace(hour=10, minute=0, second=0, microsecond=0)
    end = start + timedelta(minutes=30)

    event = {
        "summary": "AI Meeting Scheduler Test Event",
        "location": "Zoom",
        "description": "Test event created by the BIU AI Meeting Scheduler Agent.",
        "start": {
            "dateTime": start.isoformat(),
            "timeZone": TIMEZONE,
        },
        "end": {
            "dateTime": end.isoformat(),
            "timeZone": TIMEZONE,
        },
    }

    created_event = service.events().insert(
        calendarId="primary",
        body=event,
    ).execute()

    print("Calendar event created successfully.")
    print("Event summary:", created_event.get("summary"))
    print("Event link:", created_event.get("htmlLink"))


if __name__ == "__main__":
    main()
