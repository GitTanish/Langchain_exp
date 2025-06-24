from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

roq_api_key = os.getenv("GROQ_API_KEY")
if roq_api_key is not None:
    os.environ["GROQ_API_KEY"] = roq_api_key
else:
    raise ValueError("GROQ_API_KEY environment variable is not set.")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key is not None:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key


# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a smart assistant. Please answer the user's question."),
        ("user", "{question}")
    ]
)

# Ollama  LLM
llm = Ollama(model="phi:latest") 
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

st.title("OLLaMa Chatbot")
input_text = st.text_input("Ask me anything:")

if input_text:
    st.write(chain.invoke({"question": input_text}))