import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
# -----------------------------
# CONFIGURATION
# -----------------------------
API_KEY =os.getenv("GOOGLE_API_KEY")   # <-- replace with your Gemini API key
genai.configure(api_key=API_KEY)

MODEL_NAME = "models/gemini-2.5-flash"
model = genai.GenerativeModel(MODEL_NAME)

# -----------------------------
# SIMPLE TOOL FUNCTIONS
# -----------------------------
def get_leave_balance():
    return "Your remaining leave balance is: **12 days**."

def check_laptop_status():
    return "Your assigned laptop Dell Latitude 5440 is ready for pickup."

def compliance_training_status():
    return "Your Compliance training is **Pending**. Please complete it by Friday."

TOOLS = {
    "HR": get_leave_balance,
    "IT": check_laptop_status,
    "COMPLIANCE": compliance_training_status
}

# -----------------------------
# ORCHESTRATOR
# -----------------------------
def orchestrator(user_input):
    route_prompt = f"""
    You are an AI router. Read the user's message and decide:

    - If message is about salary, leaves → return HR
    - If message is about laptop, software, login issues → return IT
    - If message is about rules, policies, training → return COMPLIANCE
    - Otherwise return GENERAL

    User: "{user_input}"
    """

    route = model.generate_content(route_prompt).text.strip().upper()

    if "HR" in route:
        agent = "HR"
    elif "IT" in route:
        agent = "IT"
    elif "COMPLIANCE" in route:
        agent = "COMPLIANCE"
    else:
        agent = "GENERAL"

    if agent in TOOLS:
        return TOOLS[agent](), agent

    general_prompt = f"You are a helpful onboarding assistant. User asked: {user_input}"
    response = model.generate_content(general_prompt).text

    return response, agent


# -----------------------------
# STREAMLIT CHAT UI (with Sidebar Buttons)
# -----------------------------
st.set_page_config(page_title="Onboarding Assistant", layout="wide")

# Sidebar
with st.sidebar:
    st.markdown("## ⚡ Quick Actions")

    if st.button("HR: Leave Balance"):
        st.session_state["quick_action"] = "HR"

    if st.button("IT: Laptop Status"):
        st.session_state["quick_action"] = "IT"

    if st.button("Compliance: Training Status"):
        st.session_state["quick_action"] = "COMPLIANCE"

    st.markdown("---")
    st.markdown("### 👨‍💼 Powered by Gemini 2.5 Flash")


# Chat Header
st.markdown("<h2 style='color:#2E86C1;'>🤖 Employee Onboarding Assistant</h2>",
            unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Handle quick-action button click
if "quick_action" in st.session_state:
    tool_key = st.session_state.pop("quick_action")
    bot_response = TOOLS[tool_key]()
    st.session_state.messages.append({"role": "assistant", "content": bot_response})


# User chat input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response, agent = orchestrator(user_input)
    st.session_state.messages.append({"role": "assistant", "content": f"{response}"})


# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
