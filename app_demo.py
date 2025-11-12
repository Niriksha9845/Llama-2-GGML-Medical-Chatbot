
import streamlit as st

st.set_page_config(page_title="Albot (Demo)", layout="centered")
st.title("🩺 Albot — Demo (Shareable)")
st.write("This is a small demo version so you can show a working link to teachers/friends.")

q = st.text_input("Ask me something (try: fever, headache):")

if st.button("Get answer"):
    if not q.strip():
        st.warning("Type a question first.")
    elif "fever" in q.lower():
        st.success("Fever: often a sign your body is fighting infection. Rest + hydrate.")
    elif "headache" in q.lower():
        st.success("Headache: can be stress or dehydration. Try rest & water.")
    else:
        st.info("Sorry — demo can only answer simple prompts about fever/headache.")
