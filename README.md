# aioppgave
Prosjektet handlet om å lage en enkel chatbot i python som du kan spørre spørsmål som den kan svare.

Chatbotten fungerer ved å bruke en lang dictionary med spørsmål og svar. Inputten til brukeren blir lagret i en variabel som blir sammenlignet med en av spørmålene
i dictionarien, hvis den er der så printer botten svaret som den har til spørsmålet. En ekstra funksjon er der for å få botten til å strømme ut teksten som ChatGPT
gjør også.

Chatbotten trenger en kodeeditor og python3.

For å lage en ordentlig chatbot så kan man bruke openai sitt api, som lar deg bruke GPT 3.5, som er den som blir brukt på nettsiden deres.
Man trenger først å betale for openai sitt api.
Skaff deg en api key fra Openai sitt nettside
Installer openai modulen gjennom "pip install openai".
Bruk denne koden med api keyen som du har og så har man en fungerenede Chatbot.

import openai

openai.api_key = 'YOUR-API-KEY'

content = input("User: ")
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages =[
        {"role": "user", "content": "HOW-CHATBOT-WILL-ACT"}
    ]
)

chat_response = completion.choices[0].message.content
print(f'ChatGPT: {chat_response}')
