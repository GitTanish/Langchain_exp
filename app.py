import streamlit as st
'''
A Streamlit application for interactive retrieval-augmented question answering over the LangChain documentation using Groq's LLMs.
Features:
- Loads and splits documentation from the LangChain website.
- Embeds and indexes documents using HuggingFace sentence transformers and FAISS.
- Accepts user questions via a text input.
- Retrieves relevant context from the indexed documentation.
- Uses Groq's Llama3-70b-8192 model to answer questions based strictly on the retrieved context.
- Displays the answer and the supporting context documents.
Environment Variables:
- GROQ_API_KEY: API key for authenticating with Groq's LLM service.
Session State Keys:
- 'vector': FAISS vector store for document retrieval.
- 'embeddings': HuggingFace embeddings model.
- 'loader': WebBaseLoader instance for fetching documentation.
- 'docs': Loaded documents.
- 'text_splitter': Text splitter for chunking documents.
- 'final_documents': List of split document chunks.
Usage:
- Run the app with Streamlit.
- Enter a question about the LangChain documentation.
- View the answer and the context used for retrieval.
'''
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time

from dotenv import load_dotenv
load_dotenv()

## load the Groq API key
groq_api_key = os.environ['GROQ_API_KEY']

# SESSION STATE
if 'vector' not in st.session_state:
    st.session_state.embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2")
    st.session_state.loader=WebBaseLoader("https://python.langchain.com/docs/get_started/introduction")
    st.session_state.docs=st.session_state.loader.load()

    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
    st.session_state.vector = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

st.title("Tux Smith LangChain Documentation Retrieval")
st.write("This app retrieves documents from the LangChain documentation and allows you to interact with them using Groq's chat capabilities.")
llm = ChatGroq(
    model='llama3-70b-8192'
)

prompt = ChatPromptTemplate.from_template(
    """
    You are an AI assistant tasked with answering questions only using the provided context.

    Carefully read the following context and then answer the user's question.

    If the answer is explicitly stated in the context, provide it concisely and directly.
    If the context does not contain the answer or is insufficient to answer the question fully, state "I don't know."

    Context:
    {context}

    Question:
    {input}

    Answer:
    """
)

document_chain = create_stuff_documents_chain(llm, prompt)
retriever = st.session_state.vector.as_retriever()

retrieval_chain = create_retrieval_chain(retriever, document_chain)

prompt = st.text_input("Ask a question about the LangChain documentation:")

if prompt:
    start= time.process_time()
    response = retrieval_chain.invoke({"input":prompt})
    print('Response time:', time.process_time()-start)
    st.write(response['answer'])

    with st.expander("Context used for the answer"):
        for i, doc in enumerate(response['context']):
            st.write(f"Document {i+1}:")
            st.write(doc.page_content)
            st.write("-----------------")

