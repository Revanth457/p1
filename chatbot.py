import nltk
from nltk.chat.util import Chat, reflections
from datetime import datetime
import pytz

# Define timezone
Ind = pytz.timezone("Asia/Kolkata")

pairs = [
    (r"hi|hello", ["Hello!", "Hi there!"]),
    (r"how are you\?", ["I'm good, thanks for asking!", "I'm doing well, how about you?"]),
    (r"what is your name\?", ["I am a chatbot created by you.", "I don't have a name, but you can call me Chatbot."]),
    (r"what is the weather like\?", ["I’m not sure about the current weather. You can check a weather website for up-to-date information."]),
    (r"what time is it\?", [f"The current time is {datetime.now(Ind).strftime('%H:%M:%S')}"]),
    (r"what is the date today\?", [f"Today's date is {datetime.now(Ind).strftime('%Y-%m-%d')}"]),
    (r"what is the day today\?", [f"Today's day is {datetime.now(Ind).strftime('%A')}"]),
    (r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!", "Why did the math book look sad? Because it had too many problems."]),
    (r"what's your favorite color\?", ["I don't have personal preferences, but I think blue is a nice color."]),
    (r"tell me a fact", ["Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."]),
    (r"who created you\?", ["I was created by a developer using NLTK."]),
    (r"give me some advice", ["Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."]),
    (r"what can you do\?", ["I can help with a variety of things such as telling you the time, providing facts, and telling jokes."]),
    (r"help", ["You can ask me about the time, date, day, weather, jokes, and more. Try asking 'What is your name?' or 'Tell me a joke.'"]),
    (r"commands", ["Here are some things you can ask me: 'What is the time?', 'Tell me a joke', 'What is 5 plus 3?', 'Give me some advice', 'What can you do?', and more."]),
    (r"(.*)", ["Sorry, I don't understand that. Can you ask something else?"])
]

def nltk_chatbot():
    print("Hello! I'm a simple chatbot using NLTK. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chat.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    nltk_chatbot()
