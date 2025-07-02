# 🔍 Langchain\_exp — Multi-Tool AI Agent using LangChain & Groq

This repository implements a **multi-action AI agent** that uses [LangChain](https://python.langchain.com/) and [Groq’s LLaMA3-70B](https://groq.com/) to answer complex queries by leveraging multiple tools — all in a single reasoning loop.

> 🔗 **Repo**: [github.com/GitTanish/Langchain\_exp](https://github.com/GitTanish/Langchain_exp)

---

## 🚀 What It Does

* 🧠 Uses Groq’s blazing fast LLaMA3-70B model for reasoning
* 🧰 Combines **multiple tools** dynamically via `create_tool_calling_agent` (LangChain's modern agent framework)
* 📚 Searches **Wikipedia**, **Arxiv**, and **LangChain Docs**
* 🔍 Retrieves LangChain documentation using **FAISS** + **HuggingFace embeddings**

---

## 🔧 Tools Used

| Tool                  | Purpose                                          |
| --------------------- | ------------------------------------------------ |
| `WikipediaQueryRun`   | General knowledge from Wikipedia                 |
| `ArxivQueryRun`       | Fetching recent academic papers                  |
| `LangChain Retriever` | Custom retriever trained on LangChain agent docs |

---

## 🧰 Tech Stack

* **Python 3.11+**
* **LangChain (latest)**
* **langchain\_community** for tools/loaders/utilities
* **Groq API** via `langchain_groq`
* **FAISS** for vector search
* **HuggingFace sentence-transformers** for embeddings

---

## ⚙️ Setup Instructions

1. **Clone the Repo**

```bash
git clone https://github.com/GitTanish/Langchain_exp.git
cd Langchain_exp
```

2. **Install Requirements**

```bash
pip install -r requirements.txt
```

3. **Set Your API Key**

Create a `.env` file in the root directory and add your Groq key:

```
GROQ_API_KEY=your_groq_api_key
```

4. **Run the Agent**

```bash
python app.py
```

---

## 📌 Example Query

```text
Input:
"Search for LangChain agents and get the latest arxiv paper about agents."

Output:
[Agent invokes Wikipedia, Arxiv, and LangChain tools automatically and summarizes findings.]
```

---

## 📁 Project Structure

```
Langchain_exp/
├── app.py              # Main agent logic
├── .env                # API keys (not committed)
├── requirements.txt    # Dependencies
└── README.md           # You're here!
```

---

## 🧠 Credits

* [LangChain](https://python.langchain.com/)
* [Groq](https://groq.com/)
* [Sentence Transformers](https://www.sbert.net/)
* [FAISS](https://github.com/facebookresearch/faiss)

---

## ✅ To-Do Ideas

* [ ] Add Streamlit UI
* [ ] Enable caching of documents
* [ ] Deploy on Hugging Face or Render

---
