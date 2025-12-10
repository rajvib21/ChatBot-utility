import streamlit as st
from chatbot import get_chatbot_response


st.title("AI Chatbot 🤖")

user_input = st.text_input("Ask something:")

if st.button("Send"):
    if user_input.strip() != "":
        response = get_chatbot_response(user_input)
        st.write("**Chatbot:** ", response)
