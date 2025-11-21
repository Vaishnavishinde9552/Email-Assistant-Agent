from utils import analyze_with_gemini

def generate_followup_plan(email_text: str, meeting_date: str, meeting_time: str):
    """
    Agent 2: Generates a professional follow-up / meeting confirmation reply.
    Output = plain text only.
    """
    prompt = f"""
You are Agent 2 (Follow-up & Meeting Planner AI Assistant).

Read the user's email and generate a clean plain-text reply.

Include:
- Short summary (2–3 lines)
- Priority level (High / Medium / Low)
- Suggested follow-up date
- Professional meeting confirmation line:
    Date: {meeting_date}
    Time: {meeting_time}

Rules:
- Output strictly plain text
- Keep tone polite and professional

Email Content:
\"\"\"{email_text}\"\"\"
"""
    return analyze_with_gemini(prompt)
