"""
Main entry point for the AI Meeting Scheduler Agent.
"""

from src.meeting_agent import run_agent_cycle

def main():
    print("Welcome to the AI Meeting Scheduler Agent!")
    print("Running initial sync cycle...")
    
    try:
        run_agent_cycle()
    except Exception as e:
        print(f"An error occurred during execution: {e}")
    
    print("Process finished successfully.")

if __name__ == "__main__":
    main()
