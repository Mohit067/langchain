

# this is a static prompt kyuki user ko yaha har bar input mai apna prompt likhna padh rha h

from langchain_ollama import ChatOllama

import streamlit as st


model = ChatOllama(model="tinyllama:latest")
st.header("Research Tool")

user_input = st.text_input('Enter Your Prompts')

if st.button("Summarize"):
    if user_input:
        response = model.invoke(f"Summarize this text:\n{user_input}")
        st.write(response.content)
    else:
        st.warning("Please enter some text first.")