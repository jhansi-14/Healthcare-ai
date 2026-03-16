import streamlit as st
import requests

API_URL = "https://healthcare-ai-api-6of9.onrender.com"

st.title("Healthcare AI Assistant")

st.write("Enter your symptoms and get AI suggestions")

symptoms = st.text_input("Symptoms")

if st.button("Analyze"):

    data = {
        "symptoms": symptoms
    }

    response = requests.post(
        f"{API_URL}/health",
        json=data
    )

    st.write("Response from API:")
    st.json(response.json())