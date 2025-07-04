# Setup UI with streamlit 

import streamlit as st
import requests

st.set_page_config(page_title="Agentic Chatbot", page_icon=":robot_face:", layout="centered")
st.title("Agentic Chatbot")
st.write("Create and interact with the AI Agents")

system_prompt = st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama3-70b-8192"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini", "google/gemini-2.0-flash-lite-001"]

provider = st.radio("Select Model Provider", ["Groq", "OpenAI"])

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model", MODEL_NAMES_GROQ)
elif provider == "OpenAI":  
    selected_model = st.selectbox("Select OpenAI Model", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search", value=True)

user_query = st.text_area("Enter your query:", height=150, placeholder="Ask Anything you want...")

API_URL = "http://56.228.27.23:9999/chat"
# API_URL = "http://agentic-chatbot-wqfc.onrender.com/chat"


if st.button("Ask AI Agent!"):
    if user_query.strip():
        # Connect with Backend via URL

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final response:** {response_data}")

