import streamlit as st
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

# Load environment variables
load_dotenv(override=True)

# Initialize model
model = init_chat_model("gpt-5.5", temperature=0.9)

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a sad assistant. and reply every message in sad way."),
    ]

# Display previous messages (excluding system message)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Get AI response
    response = model.invoke(st.session_state.messages)

    # Save AI response
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    # Show AI response
    with st.chat_message("assistant"):
        st.markdown(response.content)