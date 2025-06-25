from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama

load_dotenv()

# Check for Groq API Key
if not os.getenv("GROQ_API_KEY"):
    raise EnvironmentError("GROQ_API_KEY not found in environment variables. Please set it in your .env file.")

# Create app instance
app = FastAPI(
    title="Groq LLM Chatbot",
    description="A FastAPI application that serves a Groq LLM chatbot using LangChain.",
    version="1.0.0"
)

# Define models
groq_model = ChatGroq(model="llama3-70b-8192")
ollama_model = Ollama(model="phi:latest")

# Define prompts
prompt1 = ChatPromptTemplate.from_template("Write a philosophical summary about {topic} like Fyodor Dostoevesky.")
prompt2 = ChatPromptTemplate.from_template("Write a philosophical quote about {topic} like franz kafka.")

# Add routes
add_routes(app, runnable=groq_model, path="/groq")
add_routes(app, runnable=prompt1 | groq_model, path="/summary")
add_routes(app, runnable=prompt2 | ollama_model, path="/quote")

# Optional root route
@app.get("/")
def read_root():
    return {"message": "LangChain API is running. Try POST /groq/invoke"}

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

"""
CHANGES MADE BETWEEN app.py (original version) AND app2.py (working version):

1. Fixed Critical Bug: Removed duplicate 'app = FastAPI()' at the end
   - In app.py, the second 'app = FastAPI()' overwrites the original app and deletes all added routes.
   - In app2.py, only one FastAPI instance is created and used consistently.

2. Cleaner Model Initialization:
   - app2.py creates 'groq_model' and 'ollama_model' before using them in routes.
   - app.py used 'ChatGroq(...)' inline when adding routes, then separately redefined it later — potentially confusing and error-prone.

3. Improved Prompt Design:
   - app2.py enhances prompt quality with author-specific style (e.g., "like Fyodor Dostoevsky" / "like Franz Kafka") for richer responses.

4. Added Root Endpoint for Health Check:
   - app2.py includes '@app.get("/")' to return a message when visiting the root URL.
   - This makes it easier to confirm the server is live via browser or curl.

5. General Clean-up and Best Practices:
   - app2.py maintains clearer code organization: environment loading, error checks, model & prompt setup, and route declarations are logically ordered.
   - This enhances readability, reusability, and maintainability.
"""
