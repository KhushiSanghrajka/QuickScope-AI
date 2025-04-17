# 🛠️ QuickScope AI – Multi-Agent Project Planner

QuickScope AI is a multi-agent system that takes in a project idea and generates a detailed project plan by simulating a real software team's workflow. It's designed to assist in quick project estimations, including understanding requirements, suggesting architecture, estimating resources, writing scopes, and planning timelines.

---

## 📌 Features

- 🤖 **Understanding Agent (BA)**: Extracts key goals, features, users, and constraints from the project description.
- 💻 **Developer Agent**: Defines technical architecture, technologies, and communication flow.
- 🧱 **Resource Agent (Tech Architect)**: Suggests required resources, team size, and skillsets.
- 📋 **Scope Writer Agent**: Generates a detailed scope document.
- 🕒 **Timeline Agent (Project Manager)**: Estimates time required for each phase of development.
- 🧠 **Master Agent**: Manages communication between agents, maintains flow, and handles iterations.

---

## 🧩 Architecture Overview

``` 
User Input → CTO Agent ├── Understanding Agent → Developer Agent │ ↓ ↓ ├────── Scope Writer Agent ← Resource Agent │ ↓ └──────────────────────────── Timeline Agent ↓ Final Project Plan
```
---

## ⚙️ Tech Stack

- Python 🐍
- OpenAI Agents SDK (via `openai/agents`)
- Flask (Backend API)
- AsyncOpenAI Client (Azure OpenAI Support)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/quickscope-ai.git
cd quickscope-ai
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Set up your .env file
```
OPENAI_API_KEY=your-azure-openai-api-key    (or OpenAI key)
```
### 4. Run the Flask API
```bash
python app.py
```

## 🔄 Future Enhancements
✅ Internal agent iteration logic

🔐 Guardrails to prevent hallucination and invalid plans

🧰 Integration with tools (e.g., web search, cost estimator)

🎛️ Add MCP (Multi-Agent Control Panel) for monitoring/debugging

🌐 Deploy with FastAPI + Streamlit for better UX

