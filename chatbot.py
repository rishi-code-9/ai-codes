
import random
import re

# Predefined intents, patterns and responses
intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning"],
        "responses": [
            "Hello! How can I help you?",
            "Hi! Nice to meet you.",
            "Hey! What can I do for you?"
        ]
    },

    "name": {
        "patterns": ["what is your name", "your name"],
        "responses": [
            "I am a simple chatbot.",
            "My name is ChatBot."
        ]
    },

    "study": {
        "patterns": ["help me study", "study help", "assignment"],
        "responses": [
            "Sure! Which subject are you studying?",
            "I can help you with your assignments."
        ]
    },

    "goodbye": {
        "patterns": ["bye", "goodbye", "see you"],
        "responses": [
            "Goodbye! Have a nice day.",
            "See you again!"
        ]
    }
}


# Chatbot function
def chatbot(user_input):

    user_input = user_input.lower()

    for intent in intents.values():
        for pattern in intent["patterns"]:

            if re.search(r"\b" + re.escape(pattern) + r"\b", user_input):
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand. Please try again."


# Main program
print("ChatBot: Hello! I am your chatbot.")
print("Type 'bye' to exit.")

while True:

    user = input("You: ")

    response = chatbot(user)

    print("ChatBot:", response)

    if re.search(r"\b(bye|goodbye)\b", user.lower()):
        break
