import streamlit as st

#For Displaying Title
st.title("Welcome to Streamlit")

#For Getting Text Input
name = st.text_input("Enter your Name ")

#For Getting button
if st.button("Greet me"):
    st.write("Hello ,", name)