import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("⚠ GOOGLE_API_KEY / GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Initialize Model (Gemini 2.0 Flash)
model = genai.GenerativeModel("gemini-2.0-flash")


def analyze_with_gemini(prompt: str):
    """
    Sends a given prompt to Gemini and returns the raw text response.
    """
    response = model.generate_content(prompt)
    return response.text if response and response.text else "No response from AI"
