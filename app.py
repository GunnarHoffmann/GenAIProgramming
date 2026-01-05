import streamlit as st
import random

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎲 Square Guessing Game 🎲</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Guess the square of a random number between 0 and 50!</p>", unsafe_allow_html=True)

if 'number' not in st.session_state:
    st.session_state.number = random.randint(0, 50)

st.markdown(f"<h2 style='text-align: center;'>What is the square of <span style='color: #FF5722;'>{st.session_state.number}</span>?</h2>", unsafe_allow_html=True)

guess = st.number_input("Enter your guess:", value=0.0, step=1.0, min_value=0.0)

col1, col2 = st.columns(2)

with col1:
    if st.button("Check Guess", key="check"):
        correct_square = st.session_state.number ** 2
        if guess == correct_square:
            st.success(f"🎉 Correct! The square of {st.session_state.number} is {correct_square}.")
            st.session_state.number = random.randint(0, 50)
            st.rerun()
        else:
            st.error(f"❌ Wrong! The correct square is {correct_square}. Try again or start a new game.")

with col2:
    if st.button("New Game", key="new"):
        st.session_state.number = random.randint(0, 50)
        st.rerun()