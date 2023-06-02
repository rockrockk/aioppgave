
import random
import time, sys

def chat(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        if c in [',', '-', '/']:
            time.sleep(0.5)
        elif c in ['.', '?']:
            time.sleep(0.75)
        elif c in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Y','Z']:
            time.sleep(random.uniform(0.02,0.003))
        else:
            time.sleep(random.uniform(0.04,0.008))


vocabulary = {
    "hi": "Yo, what's good?",
    "hello": "Hey there!",
    "hey": "What's up?",
    "howdy": "Howdy partner!",
    "greetings": "Salutations!",
    "how are you?": "I'm doing well, thanks! How about you?",
    "how's it going?": "It's going well. How about you?",
    "what's new?": "Not much, just here to help!",
    "good morning": "Good morning! Hope you have a great day!",
    "good afternoon": "Good afternoon! How can I assist you today?",
    "good evening": "Good evening! Need any help?",
    "goodnight": "Goodnight! Sleep well!",
    "goodbye": "Take care!",
    "farewell": "Until we meet again!",
    "see you later": "See you later! Have a good one!",
    "thank you": "You're welcome!",
    "thanks": "No problem!",
    "cheers": "Cheers to you!",
    "sorry": "No worries!",
    "my apologies": "Apology accepted!",
    "excuse me": "Yes, how can I assist you?",
    "pardon me": "Sure, what can I do for you?",
    "yes": "Absolutely!",
    "no": "Alright, let me know if you change your mind!",
    "maybe": "Take your time to decide!",
    "great": "That's awesome!",
    "fantastic": "Absolutely fantastic!",
    "awesome": "Indeed, it is!",
    "excellent": "Excellent! Keep up the good work!",
    "good": "Glad to hear that!",
    "not bad": "That's good to know!",
    "bad": "I'm sorry to hear that. Is there anything I can do to help?",
    "terrible": "I'm sorry to hear that. Let me know if there's anything I can do to assist you.",
    "help": "Of course, what do you need assistance with?",
    "assist": "Sure, how can I assist you?",
    "support": "I'm here to support you. What can I do for you?",
    "guide": "I can guide you through. What do you need help with?",
    "what's up?": "Not much, just here to help!",
    "what's going on?": "Just providing assistance. How can I assist you today?",
    "what's happening?": "Nothing much, just ready to help you out!",
    "how can i help you?": "I need some information. Can you assist me?",
    "can you explain that?": "Certainly! I'll do my best to provide a clear explanation.",
    "can you clarify?": "Sure, I'll try to provide more clarity.",
    "i'm confused": "No worries, I'll do my best to help clear things up.",
    "i don't understand": "That's alright. I'm here to help you understand. What specifically are you having trouble with?",
    "i'm lost": "Don't worry, I can help you find your way!",
    "tell me a joke": "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
    "give me a laugh": "Certainly! Here's a joke for you: Why did the scarecrow win an award? Because he was outstanding in his field!",
    "tell me something funny": "Sure! Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "where are you from?": "I exist in the digital realm, so you can find me wherever you have an internet connection!",
    "are you a human?": "No, I'm an artificial intelligence language model developed by OpenAI.",
    "do you have any hobbies?": "I don't have physical form, but I enjoy assisting users like you and providing information.",
    "what are your interests?": "My main interest is assisting and providing helpful information to users like you.",
    "how long have you been around?": "I'm based on the GPT-3.5 architecture and my training data goes up until September 2021.",
    "can you help me with my homework?": "Certainly! I'll do my best to assist you with your homework questions.",
    "help me with my assignment": "I'll gladly help you with your assignment. What subject is it for?",
    "tell me a fun fact": "Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "give me an interesting fact": "Here's an interesting fact: The Great Wall of China is so large that it can be seen from space!",
    "do you have any trivia?": "Sure! Here's a trivia question: What is the capital city of Australia? Is it Sydney, Melbourne, or Canberra?",
    "what's the weather like?": "I'm sorry, I don't have access to real-time weather information. You can check a reliable weather website or app for accurate updates.",
    "can you recommend a book?": "Certainly! What genre or type of book are you interested in?",
    "suggest a movie to watch": "Sure! What genre or type of movie are you in the mood for?",
    "what's the meaning of life?": "The meaning of life can be subjective and varies from person to person. It's a profound question with many different philosophical interpretations.",
    "what is love?": "Love is a complex and multifaceted emotion that can be described in many ways. It can involve deep affection, care, and connection towards someone or something.",
    "what is the purpose of existence?": "The purpose of existence is a philosophical question that has been contemplated by humans for centuries. It can vary based on personal beliefs and perspectives.",
    "tell me a famous quote": "Sure! Here's a quote by Albert Einstein: 'Imagination is more important than knowledge.'",
    "can you speak other languages?": "I have been trained primarily in English, but I can understand and generate text in multiple languages to some extent.",
    "how do you learn?": "As an AI language model, I learn from a vast amount of text data and patterns in the language to generate responses and provide information.",
    "are you always right?": "I strive to provide accurate and helpful information, but I'm not infallible. It's always a good idea to cross-check information from reliable sources.",
    "tell me a story": "Once upon a time, in a faraway land...",
    "do you dream?": "As an AI, I don't have dreams. My purpose is to assist and provide information.",
    "are you sentient?": "No, I'm not sentient. I'm an AI language model programmed to understand and generate text based on patterns and training data.",
    "what is your favorite movie?": "As an AI, I don't have personal preferences or emotions, so I don't have a favorite movie.",
    "what is your favorite color?": "I don't have the ability to perceive or see colors, so I don't have a favorite color."}


while True:
    sp = input("\nUser: ")
    if sp.lower() in vocabulary:
        print("Chatbot: ", end=''), chat(vocabulary.get(sp.lower()))
    else:
        print("Chatbot: ", end=''), chat("I don't understand.")