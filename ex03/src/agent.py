"""
MCP Client Agent for the AI Meeting Scheduler Agent.

This client connects to the local MCP server over stdio, discovers the
available tools, and runs an autonomous iterative workflow:

1. Fetch recent Gmail emails.
2. Parse each email as a possible meeting request.
3. If details are missing, send a clarification reply.
4. If details exist, check Google Calendar availability.
5. If available, create a calendar event and send confirmation.
6. If busy, send a polite busy reply.
7. Mark the email as processed.

The MCP server owns the tools.
This MCP client owns the decision-making workflow.
"""

import asyncio
import json
import os
import sys
from typing import Any, Dict, Optional

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


SERVER_MODULE = "src.mcp_server"


def _extract_tool_payload(result: Any) -> Dict[str, Any]:
    """
    Convert an MCP tool result into a normal Python dictionary.

    FastMCP often returns tool results as TextContent containing JSON text.
    This helper keeps the client robust if the SDK representation changes.
    """
    if hasattr(result, "structuredContent") and result.structuredContent:
        return result.structuredContent

    if hasattr(result, "structured_content") and result.structured_content:
        return result.structured_content

    if hasattr(result, "content") and result.content:
        first_item = result.content[0]

        if hasattr(first_item, "text"):
            text = first_item.text
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                return {"success": True, "raw": text}

        return {"success": True, "raw": str(first_item)}

    return {"success": False, "error": "Empty MCP tool response"}


async def call_tool(session: ClientSession, tool_name: str, arguments: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Call an MCP tool and return a clean dictionary response.
    """
    arguments = arguments or {}
    print(f"\n[MCP CLIENT] Calling tool: {tool_name}")
    print(f"[MCP CLIENT] Arguments: {arguments}")

    result = await session.call_tool(tool_name, arguments)
    payload = _extract_tool_payload(result)

    # Some MCP SDK responses wrap the real tool output inside a "result" key.
    # Unwrap it so the agent can work with a clean dictionary.
    if isinstance(payload, dict) and isinstance(payload.get("result"), dict):
        payload = payload["result"]

    print(f"[MCP CLIENT] Result: {payload}")
    return payload


def _get_email_id(email: Dict[str, Any]) -> Optional[str]:
    return email.get("id") or email.get("email_id") or email.get("message_id")


def _get_thread_id(email: Dict[str, Any]) -> Optional[str]:
    return email.get("thread_id") or email.get("threadId")


def _get_sender(email: Dict[str, Any]) -> str:
    return email.get("sender") or email.get("from") or ""


def _get_subject(email: Dict[str, Any]) -> str:
    return email.get("subject") or "Meeting request"


async def handle_email(session: ClientSession, email: Dict[str, Any]) -> None:
    """
    Handle a single email using MCP tools.
    """
    email_id = _get_email_id(email)
    thread_id = _get_thread_id(email)
    sender = _get_sender(email)
    subject = _get_subject(email)

    print("\n" + "=" * 70)
    print(f"[AGENT] Processing email: {email_id}")
    print(f"[AGENT] Subject: {subject}")
    print(f"[AGENT] Sender: {sender}")

    parsed_response = await call_tool(
        session,
        "parse_meeting_request_tool",
        {"email": email},
    )

    if not parsed_response.get("success"):
        print("[AGENT] Parser failed. Skipping email.")
        return

    parsed = parsed_response.get("parsed", {})

    if not parsed.get("is_meeting_request"):
        print("[AGENT] Decision: Not a meeting request. Skipping.")
        if email_id:
            await call_tool(session, "mark_email_as_processed_tool", {"email_id": email_id})
        return

    missing_fields = parsed.get("missing_fields", [])

    if missing_fields:
        print(f"[AGENT] Decision: Missing details: {missing_fields}")

        clarification_body = (
            "Hi,\n\n"
            "Thank you for your message. I can help schedule this meeting, "
            "but I am missing some details.\n\n"
            f"Missing details: {', '.join(missing_fields)}\n\n"
            "Please send the missing information and I will continue the scheduling process.\n\n"
            "Best,\n"
            "AI Meeting Scheduler Agent"
        )

        if sender:
            await call_tool(
                session,
                "send_reply_email_tool",
                {
                    "to_email": sender,
                    "subject": f"Re: {subject}",
                    "body": clarification_body,
                    "thread_id": thread_id,
                },
            )

        if email_id:
            await call_tool(session, "mark_email_as_processed_tool", {"email_id": email_id})

        return

    start_time = parsed.get("start_time")
    end_time = parsed.get("end_time")
    title = parsed.get("title") or subject
    location = parsed.get("location") or ""
    description = parsed.get("raw_text") or "Created by AI Meeting Scheduler MCP Agent"

    if not start_time or not end_time:
        print("[AGENT] Decision: Missing start/end time after parsing. Asking for clarification.")
        return

    availability_response = await call_tool(
        session,
        "check_calendar_availability_tool",
        {
            "start_time": start_time,
            "end_time": end_time,
        },
    )

    is_available = availability_response.get("available", False)

    if is_available:
        print("[AGENT] Decision: Calendar is available. Creating event.")

        event_response = await call_tool(
            session,
            "create_calendar_event_tool",
            {
                "title": title,
                "start_time": start_time,
                "end_time": end_time,
                "description": description,
                "location": location,
            },
        )

        event = event_response.get("event") or {}
        event_link = event.get("htmlLink", "")

        confirmation_body = (
            "Hi,\n\n"
            "Your meeting has been scheduled successfully.\n\n"
            f"Title: {title}\n"
            f"Start: {start_time}\n"
            f"End: {end_time}\n"
            f"Location: {location or 'Not specified'}\n"
            f"Calendar link: {event_link or 'Not available'}\n\n"
            "Best,\n"
            "AI Meeting Scheduler Agent"
        )

        if sender:
            await call_tool(
                session,
                "send_reply_email_tool",
                {
                    "to_email": sender,
                    "subject": f"Confirmed: {subject}",
                    "body": confirmation_body,
                    "thread_id": thread_id,
                },
            )

    else:
        print("[AGENT] Decision: Calendar is busy. Sending busy reply.")

        busy_body = (
            "Hi,\n\n"
            "Thank you for the meeting request. "
            "Unfortunately, the requested time is not available in the calendar.\n\n"
            "Please suggest another time and I will check availability again.\n\n"
            "Best,\n"
            "AI Meeting Scheduler Agent"
        )

        if sender:
            await call_tool(
                session,
                "send_reply_email_tool",
                {
                    "to_email": sender,
                    "subject": f"Re: {subject}",
                    "body": busy_body,
                    "thread_id": thread_id,
                },
            )

    if email_id:
        await call_tool(session, "mark_email_as_processed_tool", {"email_id": email_id})


async def run_agent() -> None:
    """
    Start the MCP server and run the MCP client agent workflow.
    """
    print("Starting AI Meeting Scheduler MCP Client Agent...")

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", SERVER_MODULE],
        env=os.environ.copy(),
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            print("[MCP CLIENT] Initializing session...")
            await session.initialize()

            tools_response = await session.list_tools()
            tool_names = [tool.name for tool in tools_response.tools]
            print(f"[MCP CLIENT] Available tools: {tool_names}")

            emails_response = await call_tool(
                session,
                "fetch_recent_emails_tool",
                {"max_results": 5},
            )

            if not emails_response.get("success"):
                print("[AGENT] Failed to fetch emails.")
                return

            emails = emails_response.get("emails", [])
            print(f"[AGENT] Found {len(emails)} emails to process.")

            for email in emails:
                await handle_email(session, email)

            print("\n[AGENT] MCP Agent cycle completed successfully.")


def main() -> None:
    asyncio.run(run_agent())


if __name__ == "__main__":
    main()
