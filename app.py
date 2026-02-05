import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import chatbot

load_dotenv(".env.local")

app = Flask(__name__)

frontend_url = os.getenv("FRONTEND_URL")
if frontend_url:
    CORS(app, resources={r"/*": {"origins": frontend_url}})
else:
    CORS(app)

API_KEY = os.getenv("API_KEY")


@app.get("/")
def health():
    return jsonify({"status": "ok", "message": "Chatbot API is running"})


@app.post("/chat")
def chat():
    if API_KEY:
        provided_key = request.headers.get("x-api-key", "")
        if provided_key != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    response = chatbot.get_response(message)
    return jsonify({"response": response})


def parse_bool(value, default=False):
    if value is None:
        return default
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "0.0.0.0")
    port = int(os.getenv("PORT", os.getenv("FLASK_RUN_PORT", "5000")))
    debug = parse_bool(os.getenv("FLASK_DEBUG"), default=True)
    app.run(host=host, port=port, debug=debug)
