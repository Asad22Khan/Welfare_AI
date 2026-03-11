import streamlit as st
import requests
import uuid

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="Khidmat Welfare AI",
    page_icon="🤝",
    layout="wide"
)

# ---------- SIDEBAR ----------

with st.sidebar:

    st.title("🤝 Khidmat AI")

    role = st.selectbox(
        "Select Role",
        [
            "General User",
            "Donor",
            "Donee",
            "Surveyor",
            "Admin"
        ]
    )

    st.markdown("---")

    st.write("### Session Info")

    if "thread_id" not in st.session_state:
        st.session_state.thread_id = str(uuid.uuid4())

    st.write("Thread ID:")
    st.code(st.session_state.thread_id)

    if st.button("🔄 Reset Chat"):
        st.session_state.messages = []

    st.markdown("---")

    st.success("Backend Status: Running")

# ---------- MAIN PAGE ----------

st.title("🤖 Khidmat Welfare Assistant")

st.write(
    "AI assistant for welfare registration, donations, and surveys."
)

# ---------- CHAT MEMORY ----------

if "messages" not in st.session_state:
    st.session_state.messages = []

# display history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# ---------- USER INPUT ----------

user_input = st.chat_input("Ask something...")

if user_input:

    # add role context
    message = f"Role: {role}\nUser Query: {user_input}"

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # call FastAPI
    try:

        response = requests.post(
            API_URL,
            params={
                "message": message,
                "thread_id": st.session_state.thread_id
            }
        )

        if response.status_code == 200:
            bot_reply = response.json()["response"]
        else:
            bot_reply = "⚠️ API Error"

    except Exception as e:
        bot_reply = "⚠️ Cannot connect to backend"

    # show response
    with st.chat_message("assistant"):
        st.write(bot_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )