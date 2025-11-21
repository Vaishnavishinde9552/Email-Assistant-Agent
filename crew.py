# crewAI.py
from utils import agent1_generate_replies, agent2_followup

def generate_email_pipeline(email_text):
    """
    Pipeline for generating email responses:
    1. agent1: Generates 3 types of AI replies + reminder
    2. agent2: Processes agent1 output and optionally plans next steps
    """
    # Step 1: Call agent1 (AI replies)
    agent1_responses = agent1_generate_replies(email_text)

    # Step 2: Call agent2 (planner/follow-up) with agent1 output
    agent2_output = agent2_followup(agent1_responses, email_text)

    # Combine outputs
    pipeline_output = {
        "agent1_replies": agent1_responses,
        "agent2_followup": agent2_output
    }

    return pipeline_output


# Example usage
if __name__ == "__main__":
    sample_email = """
    Hi Vaishnavi,
    We would like to schedule an interview for the Data Analyst position.
    Please let us know your available slots.
    """

    output = generate_email_pipeline(sample_email)

    print("---AGENT1 REPLIES---")
    for style, text in output["agent1_replies"].items():
        print(f"{style.upper()}:\n{text}\n")

    print("---AGENT2 FOLLOW-UP---")
    print(output["agent2_followup"])
