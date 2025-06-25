# 🧠 Philosophical Chatbot

A full-stack philosophical chatbot application that combines the power of multiple AI models to generate literary-style content. The application features a FastAPI backend integrated with LangChain and a beautiful Streamlit frontend.

## ✨ Features

- **Dual AI Models**: Leverages both Groq and Ollama for diverse responses
- **Literary Styles**: 
  - Groq generates philosophical summaries in the style of Fyodor Dostoevsky
  - Ollama creates philosophical quotes in the style of Franz Kafka
- **Real-time Interface**: Interactive Streamlit web app with responsive design
- **RESTful API**: FastAPI backend with multiple endpoints
- **Health Monitoring**: Built-in health check endpoints

## 🏗️ Architecture

```
┌─────────────────┐    HTTP    ┌──────────────────┐    LangChain    ┌─────────────┐
│   Streamlit     │ ◄────────► │    FastAPI       │ ◄─────────────► │  AI Models  │
│   Frontend      │            │    Backend       │                 │ Groq/Ollama │
└─────────────────┘            └──────────────────┘                 └─────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Groq API Key
- Ollama installed locally

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd philosophical-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi langchain langchain-groq langchain-community langserve uvicorn streamlit python-dotenv requests
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Install and start Ollama**
   ```bash
   # Install Ollama (visit https://ollama.ai for instructions)
   ollama pull phi:latest
   ```

### Running the Application

1. **Start the FastAPI backend**
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:8000`

2. **Launch the Streamlit frontend**
   ```bash
   streamlit run streamlit_app.py
   ```
   The web interface will open at `http://localhost:8501`

## 📚 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/groq/invoke` | POST | Direct Groq model access |
| `/summary/invoke` | POST | Dostoevsky-style philosophical summaries |
| `/quote/invoke` | POST | Kafka-style philosophical quotes |

### API Usage Examples

**Generate a philosophical summary:**
```bash
curl -X POST "http://localhost:8000/summary/invoke" \
     -H "Content-Type: application/json" \
     -d '{"input": {"topic": "existence"}}'
```

**Generate a philosophical quote:**
```bash
curl -X POST "http://localhost:8000/quote/invoke" \
     -H "Content-Type: application/json" \
     -d '{"input": {"topic": "solitude"}}'
```

## 🎯 Usage

1. **Open the Streamlit interface** at `http://localhost:8501`
2. **Enter topics** in either or both input fields:
   - Left column: Get a Dostoevsky-style philosophical summary
   - Right column: Get a Kafka-style philosophical quote
3. **View responses** with proper formatting and styling

## 🛠️ Project Structure

```
philosophical-chatbot/
│
├── app.py                 # FastAPI backend server
├── streamlit_app.py       # Streamlit frontend
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)

### Model Configuration

- **Groq Model**: `llama3-70b-8192` (configurable in `app.py`)
- **Ollama Model**: `phi:latest` (configurable in `app.py`)

## 🐛 Troubleshooting

### Common Issues

1. **"GROQ_API_KEY not found"**
   - Ensure your `.env` file contains the correct API key
   - Verify the `.env` file is in the root directory

2. **Ollama connection errors**
   - Make sure Ollama is running: `ollama serve`
   - Verify the model is pulled: `ollama pull phi:latest`

3. **Port conflicts**
   - FastAPI default: `localhost:8000`
   - Streamlit default: `localhost:8501`
   - Change ports in the respective files if needed

### Debug Mode

Enable debug output by checking the console logs when running the Streamlit app. API responses are printed for troubleshooting.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the AI framework
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [Streamlit](https://streamlit.io/) for the frontend framework
- [Groq](https://groq.com/) for fast AI inference
- [Ollama](https://ollama.ai/) for local model deployment

## 🔗 Useful Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LangChain Documentation](https://docs.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq API Documentation](https://console.groq.com/docs)

---

Made with ❤️ using LangChain, Groq, Ollama, and Streamlit
