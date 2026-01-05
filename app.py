import streamlit as st

st.title("Square Calculator App")

number = st.number_input("Enter a number:", value=0.0)

square = number ** 2

st.write(f"The square of {number} is {square}")