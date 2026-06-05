"""
Main logic for the AI Meeting Scheduler Agent.
Orchestrates Gmail, LLM Parser, and Calendar services.
"""

from src import gmail_service, calendar_service, llm_parser

def run_agent_cycle():
    """
    Performs one full cycle of the meeting scheduler agent.
    1. Fetches recent unread emails.
    2. Uses LLM to identify meeting requests.
    3. Extracts meeting details.
    4. Checks calendar availability.
    5. Schedules the meeting or replies with alternatives.
    6. Marks the email as processed.
    """
    print("--- Starting Agent Cycle ---")
    
    # 1. Fetch recent emails
    emails = gmail_service.fetch_recent_emails(max_results=5)
    
    for email in emails:
        print(f"\nProcessing Email ID: {email['id']} | Subject: {email['subject']}")
        
        # 2. Check if it's a meeting request
        if not llm_parser.is_meeting_request(email['body']):
            print("Skipping: Not a meeting request.")
            continue
        
        # 3. Extract details
        details = llm_parser.extract_meeting_details(email['body'])
        if not details or not details.get('date') or not details.get('time'):
            print("Handling missing details: Sending request for clarification...")
            gmail_service.send_reply(
                to_email=email['sender'],
                subject=f"Re: {email['subject']}",
                body="I've detected a meeting request, but I'm missing some details (date or time). Could you please clarify?"
            )
            gmail_service.mark_as_processed(email['id'])
            continue
            
        # 4. Check calendar availability
        # Note: In a real app, we'd combine date/time/duration into ISO strings
        start_time = f"{details['date']}T{details['time']}"
        end_time = start_time # Simple placeholder for end time
        
        is_free = calendar_service.check_availability(start_time, end_time)
        
        if is_free:
            # 5a. Create event
            calendar_service.create_calendar_event(
                title=details['title'],
                start_time=start_time,
                end_time=end_time
            )
            gmail_service.send_reply(
                to_email=email['sender'],
                subject=f"Confirmed: {details['title']}",
                body=f"Great! I've scheduled our meeting for {details['date']} at {details['time']}."
            )
        else:
            # 5b. Handle busy
            print("Calendar conflict detected. Sending 'busy' reply...")
            gmail_service.send_reply(
                to_email=email['sender'],
                subject=f"Re: {email['subject']}",
                body="I'd love to meet, but I have a conflict at that time. Would another time work?"
            )
            
        # 6. Mark processed
        gmail_service.mark_as_processed(email['id'])

    print("\n--- Agent Cycle Completed ---")

if __name__ == "__main__":
    # Allow running the agent directly for testing
    run_agent_cycle()
