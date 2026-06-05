from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/calendar",
]

TOKEN_FILE = "token.json"


def get_header(headers, name):
    for header in headers:
        if header.get("name", "").lower() == name.lower():
            return header.get("value", "")
    return ""


def main():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    service = build("gmail", "v1", credentials=creds)

    results = service.users().messages().list(
        userId="me",
        labelIds=["INBOX"],
        maxResults=5
    ).execute()

    messages = results.get("messages", [])

    if not messages:
        print("No messages found.")
        return

    print(f"Found {len(messages)} messages:\n")

    for message in messages:
        msg = service.users().messages().get(
            userId="me",
            id=message["id"],
            format="metadata",
            metadataHeaders=["Subject", "From", "Date"]
        ).execute()

        headers = msg.get("payload", {}).get("headers", [])

        subject = get_header(headers, "Subject")
        sender = get_header(headers, "From")
        date = get_header(headers, "Date")

        print("-----")
        print(f"ID: {message['id']}")
        print(f"From: {sender}")
        print(f"Subject: {subject}")
        print(f"Date: {date}")


if __name__ == "__main__":
    main()
