#Packages som man trenger for koden.
import random
import time, sys

#Strømmer ut teksten som chatbotten skal si.
def chat(s):
    for c in s:
        #Varierer farten på hvor raskt noen symboler er i forhold til andre
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

#Dictionary som holder alle spørsmål og svar som botten kan gjøre. Venstre er spørmål, høyre er svar
vocabulary = {
    "hi": "Yo, what's good?", "Hi man"
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
    "give me a laugh": "Certainly! Here's a joke for you: Why did the scarecrow win an award? Because he was outstanding in his field!",}

#While loop som gjør at brukerern kan spørre spørsmål til botten og da sjekker om botten kan svare spørsmålet
while True:
    sp = input("\nUser: ")
    #Sjekker om botten har spørsmålet i sin vocabulær og printer svaret som den har.
    if sp.lower() in vocabulary:
        print("Chatbot: ", end=''), chat(vocabulary.get(sp.lower()))
        #Slutter chatbotten om brukeren skriver "end"
    elif sp.lower() == "end":
        print("Chatbot: ", end=''), chat("Goodbye.")
        break
    #Hvis botten ikke har spørsmålet skriver den at den ikke forstår
    else:
        print("Chatbot: ", end=''), chat("I don't understand, ask me another question.")