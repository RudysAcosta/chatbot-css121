# Simple Chatbot API (University Project)

This project is a simple chatbot built in Python for a university assignment at **Essex County College (CSC 121)**.
The chatbot reads predefined responses from a JSON file and exposes them through a Flask API. A small Vue frontend is included to consume the API.

## Features
- Reads responses from `responses.json`
- Simple keyword matching
- REST API endpoint for chat
- CLI mode for local testing
- Vue home page with a mini chat UI

## Requirements
- Python 3.8+
- Flask
- Node.js 18+ (for the Vue frontend)

## Setup (Backend)

### 1. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a backend env file:

`/Users/ncrousset/Code/CSC_121/week4/chatbot/.env.local`
```env
FLASK_HOST=0.0.0.0
PORT=5050
FLASK_DEBUG=1
FRONTEND_URL=http://localhost:5173
```

## Run the API
```bash
python app.py
```

API will run on: `http://localhost:5050`

### Health check
```bash
curl http://localhost:5050/
```

### Chat endpoint
```bash
curl -X POST http://localhost:5050/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"hello"}'
```

## Run in CLI mode
```bash
python main.py
```

## Frontend (Vue)

### 1. Install dependencies
```bash
cd frontend
npm install
```

### 2. Configure environment variables
Create a frontend env file:

`/Users/ncrousset/Code/CSC_121/week4/chatbot/frontend/.env.local`
```env
VITE_API_URL=http://localhost:5050/chat
```

### 3. Run the dev server
```bash
npm run dev
```

The frontend expects the API at `http://localhost:5050/chat`.

## Project Structure
- `app.py` — Flask API
- `main.py` — CLI version
- `chatbot.py` — core logic
- `responses.json` — predefined responses
- `requirements.txt` — dependencies
- `frontend/` — Vue app

---

This is a university project for **Essex County College (CSC 121)**, focused on learning Python, JSON handling, and basic API development.
