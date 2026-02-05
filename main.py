import chatbot


def main():
    print("Bot: Hello! I am your chatbot. How can I assist you today?")
    print("Type 'exit', 'quit', or 'bye' to end the conversation.")
    print("I can talk about my name, the weather, tell you a joke and more.")

    histories = []

    while True:
        input_text = input("You: ")
        input_text = input_text.strip()

        if input_text.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! Have a great day!")
            return

        if input_text.lower() == "history":
            print("Conversation History:")
            for role, text in histories:
                print(f"{role}{text}")
            continue

        histories.append(("User -> ", input_text))
        response = chatbot.get_response(input_text)
        histories.append(("Bot -> ", response))
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
