import base64
from email.mime.text import MIMEText
from email.utils import parseaddr
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
]
TOKEN_FILE = "token.json"


def get_gmail_service():
    """
    Authenticates and returns a Gmail API service object.
    Uses token.json for authentication.
    """
    creds = None
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    except Exception as e:
        print(f"Error loading credentials from {TOKEN_FILE}: {e}")
        print("Please ensure you have run the authentication flow to create token.json.")
        return None

    try:
        service = build("gmail", "v1", credentials=creds)
        return service
    except HttpError as error:
        print(f"An error occurred while building the Gmail service: {error}")
        return None


def _get_header(headers, name):
    """Helper to extract a specific header value from a list of headers."""
    for header in headers:
        if header.get("name", "").lower() == name.lower():
            return header.get("value", "")
    return ""

def _get_email_body(payload):
    """
    Extracts the email body from the message payload.
    Handles multipart messages by prioritizing plain text.
    """
    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":
                return base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8")
            # TODO: Handle other mime types like text/html if needed for richer content.
    elif "body" in payload and "data" in payload["body"]:
        return base64.urlsafe_b64decode(payload["body"]["data"]).decode("utf-8")
    return ""


def fetch_recent_emails(max_results=10, label_ids=['INBOX']):
    """
    Fetches recent emails from the user's Gmail account using the Gmail API.
    
    Args:
        max_results (int): Maximum number of emails to fetch.
        label_ids (list): List of label IDs to filter by (e.g., ['INBOX', 'UNREAD']).
        
    Returns:
        list: A list of email dictionaries with 'id', 'thread_id', 'subject',
              'sender', 'date', 'snippet', and 'body' (if available).
              Returns an empty list if no messages are found or an error occurs.
    """
    service = get_gmail_service()
    if not service:
        return []

    emails_list = []
    try:
        # List messages
        results = service.users().messages().list(
            userId="me",
            labelIds=label_ids,
            maxResults=max_results
        ).execute()
        messages = results.get("messages", [])

        if not messages:
            print("No messages found.")
            return []

        for message in messages:
            msg_id = message["id"]
            
            # Get full message details
            msg = service.users().messages().get(
                userId="me",
                id=msg_id,
                format="full"
            ).execute()

            payload = msg.get("payload", {})
            headers = payload.get("headers", [])

            email_data = {
                "id": msg_id,
                "thread_id": msg.get("threadId"),
                "subject": _get_header(headers, "Subject"),
                "sender": _get_header(headers, "From"),
                "date": _get_header(headers, "Date"),
                "snippet": msg.get("snippet", ""),
                "body": _get_email_body(payload),
            }
            emails_list.append(email_data)

    except HttpError as error:
        print(f"An error occurred while fetching emails: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return emails_list


def send_reply_email(to_email, subject, body, thread_id=None):
    """
    Sends a reply email using the Gmail API.
    
    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        body (str): Email body content.
        thread_id (str, optional): The thread ID to reply within. If provided,
                                   the email will be sent as part of that thread.
        
    Returns:
        dict: The sent message object if successful, None otherwise.
    """
    service = get_gmail_service()
    if not service:
        return None

    try:
        message = MIMEText(body)
        clean_to_email = parseaddr(to_email)[1] or to_email
        message["to"] = clean_to_email
        message["subject"] = subject

        if thread_id:
            message["In-Reply-To"] = thread_id # Not strictly necessary for threading, but good practice
            message["References"] = thread_id # Not strictly necessary for threading, but good practice

        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")
        
        body = {"raw": raw_message}
        if thread_id:
            body["threadId"] = thread_id

        sent_message = service.users().messages().send(
            userId="me",
            body=body
        ).execute()
        print(f"Message Id: {sent_message['id']} sent successfully.")
        return sent_message

    except HttpError as error:
        print(f"An error occurred while sending email: {error}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def mark_as_processed(email_id):
    """
    Marks an email as processed by removing the 'UNREAD' label and adding a 'PROCESSED' label.
    
    Args:
        email_id (str): The ID of the email to mark.
        
    Returns:
        bool: True if successful, False otherwise.
    """
    service = get_gmail_service()
    if not service:
        return False

    try:
        # Define the labels to remove and add
        remove_labels = ["UNREAD"]
        # TODO: Consider creating a "PROCESSED" label if it doesn't exist.
        add_labels = [] 

        service.users().messages().modify(
            userId="me",
            id=email_id,
            body={"removeLabelIds": remove_labels, "addLabelIds": add_labels}
        ).execute()
        print(f"Email {email_id} marked as processed (UNREAD label removed).")
        return True

    except HttpError as error:
        print(f"An error occurred while marking email as processed: {error}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def send_reply(to_email, subject, body, thread_id=None):
    """
    Backward-compatible wrapper used by meeting_agent.py.

    Delegates to send_reply_email so the orchestration code can call
    send_reply() while the Gmail implementation remains in send_reply_email().
    """
    return send_reply_email(
        to_email=to_email,
        subject=subject,
        body=body,
        thread_id=thread_id,
    )
