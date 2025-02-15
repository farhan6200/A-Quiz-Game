import streamlit as st
import random

st.title('Are you smarter than a 5th grader?')
st.write('This quiz will test your knowledge about general knowledge.')
st.write('I am still learning, so there may be some errors.')
st.markdown("-------------------------------")
# Define the questions and answers

questions = {
    "what is the name of the president of the united states?":"donald trump",
    "what is the capital of united states?":"washington d.c.",
    "who invented the tesla coil?":"nikola Tesla",
    "what is the name of the famous painting by vincent van gogh?":"starry night",
    "what is the name of the largest island in the world?":"greenland",
    "who is the current president of canada?":"Justin Trudeau",
    "what is the name of the largest ocean in the world?":"atlantic ocean",
    "what is the name of the longest river in the world?":"nile river",
    "who is the author of one piece manga series?":"eiichiro Oda",
    "what is the name of the largest desert in the world?":"sahara desert"
    

}
total_questions = 5
selected_questions = random.sample(list(questions.keys()), total_questions)

# Initialize session state to store answers
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

st.subheader("Quiz Questions:")

# Display questions with input fields
for idx, question in enumerate(selected_questions, start=1):
    st.write(f"**{idx}. {question}**")
    user_answer = st.text_input(f"Your answer for question {idx}:", key=f"q{idx}")
    st.session_state.quiz_answers[question] = user_answer.strip().lower()

# Submit Button
if st.button("Submit Quiz"):
    score = 0

    st.markdown("### Results:")

    for question in selected_questions:
        correct_answer = questions[question].lower()
        user_answer = st.session_state.quiz_answers.get(question, "")

        if user_answer == correct_answer:
            st.success(f"✅ Correct! {question}")
            score += 1
        else:
            st.error(f"❌ Wrong! The correct answer was: **{questions[question]}**")

    # Display Final Score
    st.markdown(f"## 🎯 Your Final Score: **{score}/{total_questions}**")
    st.write("Thanks for playing! 😊")
