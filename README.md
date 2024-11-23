# Chatbot with Python and NLTK

This repository contains a simple rule-based chatbot implemented in Python, using the Natural Language Toolkit (NLTK) for basic text preprocessing. The chatbot identifies user intents based on predefined keywords and responds accordingly with canned responses.

---

## Features

- **Intent Detection**: The chatbot recognizes basic user intents such as greetings, goodbyes, and expressions of thanks using keyword matching.
- **Response Templates**: Each intent is mapped to a list of prewritten responses, randomly selected to provide variety.
- **Text Preprocessing**: The user input is cleaned by:
  - Converting to lowercase.
  - Removing numbers and punctuation.
- **Interactive Conversation**: The chatbot runs in a loop, allowing continuous interaction until the user types "exit."

---

## Requirements

- Python 3.6 or above
- [NLTK Library](https://www.nltk.org/)

---

## How It Works

1. **Preprocessing User Input**  
   The `preprocess_text` function standardizes user input by:
   - Converting to lowercase.
   - Stripping numbers and punctuation using `re` and `string` modules.

2. **Identifying Intent**  
   The `get_intent` function checks the processed input against predefined sets of keywords for intents:
   - **Greetings**: Keywords like `hi`, `hello`, `hey`, etc.
   - **Goodbyes**: Keywords like `bye`, `goodbye`, `see you`, etc.
   - **Thanks**: Keywords like `thanks`, `thank you`, etc.
   - **Default**: A fallback intent for unrecognized inputs.

3. **Generating Responses**  
   Each intent is linked to a list of potential responses in the `responses` dictionary. A random response is chosen to keep the conversation engaging.

4. **Conversation Loop**  
   The chatbot operates in an interactive loop, responding to user inputs until the user types "exit".

---

## Example Interaction

```
Chatbot: Hi! I'm your friendly chatbot. Type 'exit' to end the conversation.
You: Hello
Chatbot: Hi there! What can I do for you?
You: Thank you!
Chatbot: You're most welcome!
You: Goodbye
Chatbot: See you later!
```

---

