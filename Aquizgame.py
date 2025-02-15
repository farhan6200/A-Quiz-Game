# Select random questions
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
