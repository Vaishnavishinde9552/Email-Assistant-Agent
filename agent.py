from utils import analyze_with_gemini

def generate_email_responses(email_text):
    """
    Generates 4 types of replies for the given email:
    1. Professional Reply
    2. Friendly Reply
    3. Short Reply
    4. Reminder Reply
    """
    replies = {}

    replies['professional_reply'] = analyze_with_gemini(
        f"You are an AI Email Writing Assistant. Write a professional reply for the email:\n\n{email_text}"
    )

    replies['friendly_reply'] = analyze_with_gemini(
        f"You are an AI Email Writing Assistant. Write a friendly reply for the email:\n\n{email_text}"
    )

    replies['short_reply'] = analyze_with_gemini(
        f"You are an AI Email Writing Assistant. Write a short, concise reply (1-2 lines) for the email:\n\n{email_text}"
    )

    replies['reminder_reply'] = analyze_with_gemini(
        f"You are an AI Email Writing Assistant. Write a polite reminder reply for the email:\n\n{email_text}"
    )

    return replies
