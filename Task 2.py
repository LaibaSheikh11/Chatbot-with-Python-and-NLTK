import nltk
import random
import string
import re

# Download the NLTK resources (if not already downloaded)
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

# Preprocessing the input text
def preprocess_text(text):
    """
    Preprocess user input by converting to lowercase,
    removing numbers, and stripping punctuation.
    """
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# Response templates for various intents
responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Greetings! How may I assist you?",
        "How can I help you, sir!"
    ],
    "goodbye": [
        "Goodbye! Have a great day!",
        "See you later!",
        "Take care!",
        "Have a good day!",
        "Nice to meet you!"
    ],
    "thanks": [
        "You're welcome!",
        "No problem!",
        "You're most welcome!",
        "Happy to help!"
    ],
    "default": [
        "I'm not sure I understand. Could you rephrase?",
        "Could you provide more details?",
        "I'm here to help. Can you clarify?",
        "I'm sorry, I don't understand. Can you explain?"
    ]
}

# Function to determine the intent of the user's message
def get_intent(user_input):
    """
    Identify the user's intent based on specific keywords.
    """
    user_input = preprocess_text(user_input)
    greetings = {"hi", "hello", "hey", "howdy"}
    goodbyes = {"bye", "goodbye", "see you", "later"}
    thanks = {"thank", "thanks", "thank you"}

    if any(greet in user_input for greet in greetings):
        return "greeting"
    elif any(bye in user_input for bye in goodbyes):
        return "goodbye"
    elif any(thank in user_input for thank in thanks):
        return "thanks"
    else:
        return "default"

# Main chatbot function
def chatbot():
    """
    A simple rule-based chatbot that interacts with the user
    based on predefined intents and responses.
    """
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! It was great talking to you!")
            break

        # Determine intent and fetch response
        intent = get_intent(user_input)
        response = random.choice(responses[intent])
        print(f"Chatbot: {response}")

# Entry point for the script
if __name__ == "__main__":
    chatbot()
