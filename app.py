from flask import Flask, jsonify, request
import chatbot

app = Flask(__name__)


@app.get("/")
def health():
    return jsonify({"status": "ok", "message": "Chatbot API is running"})


@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    response = chatbot.get_response(message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
