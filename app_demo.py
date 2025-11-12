import streamlit as st

def generate_response(prompt):
    prompt = prompt.lower()
    if "fever" in prompt:
        return "Fever is a temporary rise in body temperature often caused by infections."
    if "headache" in prompt:
        return "Headaches can be due to stress, dehydration, or lack of sleep — rest and fluids help."
    return "This is a demo reply. For real medical advice, consult a healthcare professional."

st.set_page_config(page_title="Albot — Demo", layout="centered")
st.title("Albot — Demo (Lightweight)")
st.write("This is a **small demo** version (safe for deploy).")

query = st.text_input("Ask a medical-related question:")
if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        resp = generate_response(query)
    st.success(resp)
