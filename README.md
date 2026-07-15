# 🤖 Nyrion AI — Build Your Own AI Assistant in Python

A fully working **AI Assistant** built from scratch using **Python (FastAPI)**, **React (Vite + TypeScript)**, and **Ollama**.

Nyrion AI implements a complete **Retrieval-Augmented Generation (RAG)** pipeline with document upload, semantic search, manual knowledge management, local Large Language Model (LLM) inference, vector search, and an interactive web dashboard.

> Built as an educational project to understand how modern AI assistants like ChatGPT, Perplexity, and enterprise RAG systems work internally.

---

# 🌟 Features

| Feature | Description |
|----------|-------------|
| 🤖 Local AI Chat | Chat with Llama 3.2 running locally using Ollama |
| 📄 PDF & TXT Upload | Upload documents and build your own AI knowledge base |
| 🧠 Manual Knowledge Base | Teach the AI new information directly from the application |
| 🔍 Semantic Search | Finds the most relevant document chunks using embeddings |
| 📚 Vector Database | Stores document embeddings for fast retrieval |
| ⚡ RAG Pipeline | AI answers based on retrieved context instead of guessing |
| 📊 Dashboard | View AI system overview |
| 🗂 Database Manager | Manage uploaded documents |
| 🏆 Benchmark | Display AI system information |
| ⚙ Settings | Application configuration page |
| 🌌 Premium Splash Screen | Animated startup screen with glowing effects |

---

# 🧠 How It Works

```
                User Question
                      │
                      ▼
         Generate Text Embedding
                      │
                      ▼
             Vector Database Search
                      │
                      ▼
        Retrieve Relevant Document Chunks
                      │
                      ▼
              Build Prompt Context
                      │
                      ▼
              Llama 3.2 (Ollama)
                      │
                      ▼
                Final AI Response
```

The AI first searches your uploaded documents and manually added knowledge before generating an answer.

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- PyPDF
- Ollama

## Frontend

- React
- TypeScript
- Vite
- Axios
- React Router
- Framer Motion
- Lucide React

## AI Models

- Llama 3.2
- nomic-embed-text

---

# 📁 Project Structure

```
Nyrion-AI
│
├── backend
│   ├── api
│   ├── algorithms
│   ├── database
│   ├── embeddings
│   ├── llm
│   ├── models
│   ├── uploads
│   ├── utils
│   ├── requirements.txt
│   └── main.py
│
├── frontend
│   ├── public
│   ├── src
│   │   ├── components
│   │   ├── layouts
│   │   ├── pages
│   │   ├── services
│   │   ├── styles
│   │   └── App.tsx
│   │
│   ├── package.json
│   └── vite.config.ts
│
├── README.md
└── .gitignore
```

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/Dannyy69/Nyrion-AI.git

cd Nyrion-AI
```

---

## 2. Install Ollama

Download Ollama

https://ollama.com

Pull the required models

```bash
ollama pull llama3.2

ollama pull nomic-embed-text
```

Verify

```bash
ollama list
```

---

## 3. Backend Setup

Create virtual environment

```bash
cd backend

python -m venv venv
```

Activate environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run backend

```bash
uvicorn api.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## 4. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend

```
http://localhost:5173
```

---

# 📄 Supported Documents

Current supported formats

- PDF
- TXT

Uploaded documents are automatically

- Parsed
- Split into chunks
- Converted into embeddings
- Indexed
- Stored inside the vector database
- Made searchable by the AI

---

# 🧠 Manual Knowledge Base

You can teach the AI new information.

Example

Question

```
What is FastAPI?
```

Answer

```
FastAPI is a modern, high-performance Python framework for building APIs using Python type hints.
```

The AI stores this information and uses it in future conversations.

---

# 🤖 AI Chat Workflow

```
User Message
      │
      ▼
Generate Embedding
      │
      ▼
Semantic Search
      │
      ▼
Retrieve Context
      │
      ▼
Create Prompt
      │
      ▼
Llama 3.2
      │
      ▼
AI Response
```

---

# 🌐 REST API

## System

```
GET /
```

```
GET /system/info
```

---

## Chat

```
POST /chat
```

---

## Upload

```
POST /upload
```

---

## Knowledge Base

```
POST /knowledge
```

---

## Documents

```
GET /documents
```

```
DELETE /documents/{id}
```

---

# 📊 Application Pages

- 🏠 Dashboard
- 💬 Chat
- 🔍 Search
- 📚 Database
- 🧠 Knowledge Base
- 📈 Benchmark
- ⚙ Settings

---

# 🎨 User Interface

The application includes

- Premium Splash Screen
- Dark Theme
- Animated Startup
- Responsive Sidebar
- Modern Dashboard
- AI Chat Interface
- Knowledge Management
- Document Upload
- Database Viewer

---

# 📸 Screenshots

After deployment you can add screenshots inside

```
screenshots/

dashboard.png

chat.png

database.png

knowledge.png

upload.png
```

---

# 🔮 Future Improvements

- User Authentication
- Persistent Database Storage
- Conversation History
- Streaming AI Responses
- Voice Assistant
- AI Agents
- Multi-user Support
- Cloud Deployment
- Mobile Responsive Dashboard
- Docker Support

---

# 📜 License

MIT License

---

# 👨‍💻 Author

## Danish Shetty

Computer Science Engineering Student

GitHub

https://github.com/Dannyy69

Built to learn and demonstrate

- FastAPI
- Python
- React
- TypeScript
- Ollama
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Local Large Language Models
- AI Application Development

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

GitHub Repository

https://github.com/Dannyy69/Nyrion-AI

---

**Made with ❤️ by Danish Shetty**