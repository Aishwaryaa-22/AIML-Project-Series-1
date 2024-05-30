responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I am a simple chatbot created using Python.",
    "fine": "That's great.",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "thanks": "You're welcome!",
    "what can you do": "I can chat with you and help answer some questions.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what's the weather like": "I'm not sure about the current weather, but I hope it's nice where you are!",
    "who created you": "I was created by a developer using Python.",
    "how old are you": "I'm as old as the code that runs me!",
    "do you like music": "I don't have preferences, but music is a wonderful thing!",
}
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: " + responses["bye"])
            break
        response = get_response(user_input)
        print("Chatbot: " + response)

if __name__ == "__main__":
    chat()
