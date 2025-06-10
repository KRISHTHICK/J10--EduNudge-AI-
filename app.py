import streamlit as st
from agent import ask_ai_agent
from quiz_engine import generate_quiz
from nudger import show_study_nudge

st.set_page_config(page_title="EduNudge AI", layout="wide")
st.title("📚 EduNudge AI – Your Personal Study Companion")

tab1, tab2, tab3 = st.tabs(["🧠 Ask AI", "📝 Daily Quiz", "🔔 Nudges"])

with tab1:
    st.subheader("🧠 Ask the AI Coach")
    query = st.text_input("What concept are you struggling with?")
    if query:
        st.markdown(ask_ai_agent(query))

with tab2:
    st.subheader("📤 Upload Notes (PDF/Text) for Quiz")
    uploaded_file = st.file_uploader("Upload your study material", type=["pdf", "txt"])
    if uploaded_file:
        quiz = generate_quiz(uploaded_file)
        st.markdown("### 📝 Your Quiz")
        for q in quiz:
            st.write(f"- {q}")

with tab3:
    st.subheader("⏰ Study Nudges")
    if st.button("Send Me a Nudge"):
        st.info(show_study_nudge())
