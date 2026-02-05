# Simple Chatbot API (University Project)

This project is a simple chatbot built in Python for a university assignment at **Essex County College (CSC 121)**.  
The chatbot reads predefined responses from a JSON file and exposes them through a Flask API.

## Features
- Reads responses from `responses.json`
- Simple keyword matching
- REST API endpoint for chat
- CLI mode for local testing

## Requirements
- Python 3.8+
- Flask

## Setup

### 1. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the API
```bash
python app.py
```
API will run on: http://localhost:5000

### Health check
```bash
curl http://localhost:5000/
```

### Chat endpoint
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"hello"}'
```
