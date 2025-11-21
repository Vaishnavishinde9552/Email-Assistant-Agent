import streamlit as st
from datetime import datetime
from agent import generate_email_responses
from agent2 import generate_followup_plan

st.set_page_config(page_title="AI Email Assistant", layout="wide")
st.title("📧 AI Email Assistant ✨")

# ---------- Step 1: Email Input ----------
st.subheader("Step 1: Paste Your Email")
email_text = st.text_area("📩 Paste Email Content Here", height=200)

# ---------- Step 2: Generate AI Replies ----------
st.subheader("Step 2: Generate AI Replies")
if st.button("Generate Replies"):
    if not email_text.strip():
        st.error("⚠ Please enter an email first.")
    else:
        with st.spinner("⏳ Generating AI responses..."):
            data = generate_email_responses(email_text)

        col1, col2 = st.columns(2)

        with col1:
            st.success("✨ Professional Reply")
            st.text_area("Professional", value=data.get("professional_reply"), height=150)

            st.warning("⚡ Short Reply")
            st.text_area("Short", value=data.get("short_reply"), height=100)

        with col2:
            st.info("😊 Friendly Reply")
            st.text_area("Friendly", value=data.get("friendly_reply"), height=150)

            st.info("⏰ Reminder Reply")
            st.text_area("Reminder", value=data.get("reminder_reply"), height=100)

# ---------- Step 3: Follow-Up & Meeting Planner ----------
st.write("---")
st.subheader("Step 3: Follow-Up & Meeting Planner")

col_date, col_time = st.columns(2)
with col_date:
    selected_date = st.date_input("Select Date")
with col_time:
    selected_time = st.time_input("Select Meeting Time")

scheduled_datetime = datetime.combine(selected_date, selected_time)

if st.button("Generate Follow-up Plan"):
    if not email_text.strip():
        st.error("⚠ Please enter an email first.")
    else:
        with st.spinner("⏳ Generating follow-up plan..."):
            output = generate_followup_plan(
                email_text,
                meeting_date=selected_date.strftime("%Y-%m-%d"),
                meeting_time=selected_time.strftime("%I:%M %p")
            )
        st.subheader("📝 Follow-up Plan")
        st.text_area("Follow-up Output", value=output, height=200)

        st.subheader("⏰ Meeting Scheduled")
        st.success(f"Meeting scheduled for **{scheduled_datetime}**")

st.write("---")
st.caption("Powered by Gemini 2.0 Flash ✨")

