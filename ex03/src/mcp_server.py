"""
MCP Server for the AI Meeting Scheduler Agent.

This server exposes the project's existing capabilities as MCP tools:
- Gmail tools
- Calendar tools
- Meeting parsing tools

The business logic remains in the existing service files.
This file only wraps those functions as MCP tools.
"""

from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from src.gmail_service import fetch_recent_emails, send_reply_email, mark_as_processed
from src.calendar_service import check_availability, create_calendar_event
from src.llm_parser import parse_email


mcp = FastMCP("AI Meeting Scheduler MCP Server")


@mcp.tool()
def fetch_recent_emails_tool(max_results: int = 5) -> Dict[str, Any]:
    """
    Fetch recent emails from the Gmail inbox.

    Args:
        max_results: Maximum number of emails to fetch.

    Returns:
        A dictionary containing the fetched emails.
    """
    try:
        emails = fetch_recent_emails(max_results=max_results)
        return {
            "success": True,
            "emails": emails,
            "count": len(emails),
        }
    except Exception as error:
        return {
            "success": False,
            "error": str(error),
            "emails": [],
            "count": 0,
        }


@mcp.tool()
def parse_meeting_request_tool(email: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parse an email and extract meeting request details.

    Args:
        email: Email dictionary with subject, sender, body/snippet, and id.

    Returns:
        Parsed meeting request data.
    """
    try:
        parsed = parse_email(email)
        return {
            "success": True,
            "parsed": parsed,
        }
    except Exception as error:
        return {
            "success": False,
            "error": str(error),
            "parsed": {
                "is_meeting_request": False,
                "missing_fields": [],
            },
        }


@mcp.tool()
def check_calendar_availability_tool(start_time: str, end_time: str) -> Dict[str, Any]:
    """
    Check whether the user's primary Google Calendar is free.

    Args:
        start_time: Meeting start time in ISO format.
        end_time: Meeting end time in ISO format.

    Returns:
        Availability result.
    """
    try:
        is_available = check_availability(start_time, end_time)
        return {
            "success": True,
            "available": is_available,
        }
    except Exception as error:
        return {
            "success": False,
            "error": str(error),
            "available": False,
        }


@mcp.tool()
def create_calendar_event_tool(
    title: str,
    start_time: str,
    end_time: str,
    description: str = "",
    location: str = "",
) -> Dict[str, Any]:
    """
    Create a calendar event in the user's primary Google Calendar.

    Args:
        title: Event title.
        start_time: Event start time in ISO format.
        end_time: Event end time in ISO format.
        description: Optional event description.
        location: Optional event location.

    Returns:
        Created event details.
    """
    try:
        event = create_calendar_event(
            title=title,
            start_time=start_time,
            end_time=end_time,
            description=description,
            location=location,
        )

        if not event:
            return {
                "success": False,
                "error": "Calendar event was not created.",
                "event": None,
            }

        return {
            "success": True,
            "event": {
                "id": event.get("id"),
                "summary": event.get("summary"),
                "htmlLink": event.get("htmlLink"),
            },
        }
    except Exception as error:
        return {
            "success": False,
            "error": str(error),
            "event": None,
        }


@mcp.tool()
def send_reply_email_tool(
    to_email: str,
    subject: str,
    body: str,
    thread_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Send a Gmail reply email.

    Args:
        to_email: Recipient email address.
        subject: Email subject.
        body: Email body.
        thread_id: Optional Gmail thread ID for replying in context.

    Returns:
        Send result.
    """
    try:
        result = send_reply_email(
            to_email=to_email,
            subject=subject,
            body=body,
            thread_id=thread_id,
        )
        return {
            "success": bool(result),
            "result": result,
        }
    except Exception as error:
        return {
            "success": False,
            "error": str(error),
        }


@mcp.tool()
def mark_email_as_processed_tool(email_id: str) -> Dict[str, Any]:
    """
    Mark an email as processed/read.

    Args:
        email_id: Gmail message ID.

    Returns:
        Processing result.
    """
    try:
        result = mark_as_processed(email_id)
        return {
            "success": bool(result),
            "result": result,
        }
    except Exception as error:
        return {
            "success": False,
            "error": str(error),
        }


if __name__ == "__main__":
    mcp.run()
