import streamlit as st
import random

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎲 Square Guessing Game 🎲</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Guess the square of a random number between 0 and 50!</p>", unsafe_allow_html=True)

if 'number' not in st.session_state:
    st.session_state.number = random.randint(0, 50)

if 'guess' not in st.session_state:
    st.session_state.guess = 0.0

if 'show_success' not in st.session_state:
    st.session_state.show_success = False

if st.session_state.show_success:
    st.success(f"🎉 Correct! The square of {st.session_state.last_number} is {st.session_state.last_square}.")
    st.session_state.show_success = False

st.markdown(f"<h2 style='text-align: center;'>What is the square of <span style='color: #FF5722;'>{st.session_state.number}</span>?</h2>", unsafe_allow_html=True)

guess = st.number_input("Enter your guess:", value=st.session_state.guess, step=1.0, min_value=0.0)

col1, col2 = st.columns(2)

with col1:
    if st.button("Check Guess", key="check"):
        correct_square = st.session_state.number ** 2
        if guess == correct_square:
            st.session_state.last_number = st.session_state.number
            st.session_state.last_square = correct_square
            st.session_state.show_success = True
            st.session_state.number = random.randint(0, 50)
            st.session_state.guess = 0.0
            st.rerun()
        else:
            st.error(f"❌ Wrong! The correct square is {correct_square}. Try again or start a new game.")
            st.session_state.guess = 0.0

with col2:
    if st.button("New Game", key="new"):
        st.session_state.number = random.randint(0, 50)
        st.session_state.guess = 0.0
        st.rerun()