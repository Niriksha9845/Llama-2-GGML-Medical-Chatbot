# app_demo.py
import streamlit as st

st.set_page_config(page_title="AIBot (Demo)", layout="centered")

st.title("AIBot — Demo (Lightweight)")

st.write("Hi! This is a lightweight demo so you can share the app quickly.\n"
         "It uses a small fallback responder instead of heavy ML dependencies.")

prompt = st.text_input("Ask me anything medical-related:", placeholder="e.g. fever", key="q")
if st.button("Send") or (prompt and st.session_state.get("q_submit", False) is False):
    # Simple fallback logic (same style as the project)
    def generate_response(prompt_text: str) -> str:
        p = prompt_text.lower()
        if "fever" in p:
            return "Fever is a temporary rise in body temperature, often due to infection."
        if "headache" in p:
            return "Headaches can be caused by stress, dehydration, or lack of sleep. Try resting & drinking water."
        return "I'm not sure. This is a demo — full model requires extra setup."

    answer = generate_response(prompt)
    st.markdown("**Answer:**")
    st.info(answer)
