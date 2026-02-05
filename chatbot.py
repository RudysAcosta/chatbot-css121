import json
import os


def load_responses():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "responses.json")
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "responses.json file not found"}


def get_response(input_text):
    responses = load_responses()

    if not input_text:
        return "Can you provide some input text?"

    input_text = input_text.strip().lower()

    for key in responses:
        if key in input_text:
            return responses[key]

    return "I'm sorry, I didn't understand that. Can you please rephrase?"


def chatbot(input_text=None):
    try:
        response = get_response(input_text)
        print(f"Bot: {response}")
    except Exception as e:
        print(f"Error: {e}")
