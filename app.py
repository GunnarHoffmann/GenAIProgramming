import streamlit as st
import random

st.title("Square Guessing Game")

if 'number' not in st.session_state:
    st.session_state.number = random.randint(0, 100)

st.write(f"What is the square of {st.session_state.number}?")

guess = st.number_input("Enter your guess:", value=0.0, step=1.0)

if st.button("Check Guess"):
    correct_square = st.session_state.number ** 2
    if guess == correct_square:
        st.success("Correct! Well done.")
        st.session_state.number = random.randint(0, 100)  # New number
        st.rerun()  # Refresh to show new number
    else:
        st.error(f"Wrong! The correct square is {correct_square}. Try again.")