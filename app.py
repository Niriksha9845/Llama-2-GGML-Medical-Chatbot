import streamlit as st
from model import *  # assuming model.py has your chatbot logic

st.set_page_config(page_title="AIbot - Medical Chat Assistant 🤖", page_icon="🩺")

st.title("🩺 AIbot – Your Medical Chat Assistant")
st.write("Hi! I’m NavyaBot, a simple chatbot built using Llama-2 💬")

# Input box
user_input = st.text_input("Ask me anything medical-related:")

# When user types something
if user_input:
    try:
        # If model.py has a function like `generate_response`, call it
        response = generate_response(user_input)
        st.write("**AIbot:**", response)
    except Exception as e:
        st.error(f"Error: {e}")
