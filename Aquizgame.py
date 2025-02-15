import streamlit as st
import random

st.title("Are You Smarter Than a 5th Grader? 🤔")
st.write("Test your general knowledge with this fun quiz!")
st.markdown("---")

# Define the questions and answers (with updated answers)
questions = {
    "Who is the current President of the United States?": "Joe Biden",
    "What is the capital of the United States?": "Washington D.C.",
    "Who invented the Tesla coil?": "Nikola Tesla",
    "What is the name of the famous painting by Vincent van Gogh?": "Starry Night",
    "What is the name of the largest island in the world?": "Greenland",
    "Who is the Prime Minister of Canada?": "Justin Trudeau",
    "What is the largest ocean in the world?": "Pacific Ocean",
    "What is the longest river in the world?": "Nile River",
    "Who is the author of the One Piece manga series?": "Eiichiro Oda",
    "What is the name of the largest desert in the world?": "Sahara Desert"
}

total_questions = 5

# Store selected questions in session_state so they persist between reruns
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = random.sample(list(questions.keys()), total_questions)

# Also initialize quiz_answers if not already
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

st.subheader("Quiz Questions:")

# Display questions and collect answers
for idx, question in enumerate(st.session_state.selected_questions, start=1):
    st.write(f"**{idx}. {question}**")
    user_answer = st.text_input(f"Your answer for question {idx}:", key=f"q{idx}")
    st.session_state.quiz_answers[question] = user_answer.strip().lower()

# Process answers on submission
if st.button("Submit Quiz"):
    score = 0
    st.markdown("### Results:")
    for question in st.session_state.selected_questions:
        correct_answer = questions[question].lower()
        user_answer = st.session_state.quiz_answers.get(question, "")
        if user_answer == correct_answer:
            st.success(f"✅ Correct! {question}")
            score += 1
        else:
            st.error(f"❌ Wrong! The correct answer was: **{questions[question]}**")
    st.markdown(f"## 🎯 Your Final Score: **{score}/{total_questions}**")
    st.write("Thanks for playing! 😊")
