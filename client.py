import requests
import streamlit as st

def get_groq_response(input_text):
    response = requests.post(
        "http://localhost:8000/summary/invoke",
        json={"input": {"topic": input_text}} 
    )
    data = response.json()
    print("🔍 API Response:", data)

    if isinstance(data.get("output"), dict):
        return data["output"].get("content", "No content")
    return data.get("output", "No output")

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/quote/invoke",
        json={"input": {"topic": input_text}}
    )
    data = response.json()
    print("🔍 API Response:", data)

    if isinstance(data.get("output"), dict):
        return data["output"].get("content", "No content")
    return data.get("output", "No output")

#st.set_page_config(page_title="Philosophical Chatbot", page_icon="🧠", layout="centered")

# Title
st.title("🧠 Philosophical Chatbot")
st.markdown("Chat with two minds: **Groq** for summaries and **Ollama** for quotes.")

# Input Fields in Two Columns
col1, col2 = st.columns(2)

with col1:
    input_text = st.text_input("✍️ Write a topic for Groq summary")

with col2:
    input_text2 = st.text_input("💭 Write a topic for Ollama quote")

# Groq Response
if input_text:
    with st.spinner("Generating summary..."):
        groq_response = get_groq_response(input_text)
    st.success("✅ Groq Summary")
    st.write(groq_response)

# Ollama Response
if input_text2:
    with st.spinner("Generating quote..."):
        ollama_response = get_ollama_response(input_text2)
    st.info("💡 Ollama Quote")
    st.write(ollama_response)

# Footer
st.markdown("---")
st.caption("Made with ❤️ using LangChain, Groq, Ollama, and Streamlit")