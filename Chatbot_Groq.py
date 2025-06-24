from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

# Set Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key is not None:
    os.environ["GROQ_API_KEY"] = groq_api_key
else:
    raise ValueError("GROQ_API_KEY environment variable is not set.")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key is not None:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please answer the user's question."),
        ("user", "{question}")
    ]
)

# Streamlit 
st.title("Groq LLM Chatbot")
input_text = st.text_input("Ask a question:")

# Groq LLM
llm = ChatGroq(model="llama3-70b-8192")

# Create chain
chain = prompt | llm | StrOutputParser()

# Handle input
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
