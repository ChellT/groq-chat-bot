

from groq import Groq
from dotenv import load_dotenv
import os

#setting up api key
load_dotenv(dotenv_path=".env.txt")
api_key = os.getenv("GROQ_API_KEY")


client = Groq(api_key=api_key)

#starting the converstaion with Groq
username = input("Welcome, What is your name?:  ")
print(f"\033[1mConsole:\033[0m Hello {username}! welcome to the Groq chatbot, you can start chatting now!\n To leave the converstaion, you can just say Leave, Exit, Stop, Or Goodbye!\n Whatever you are comfortable with")

messages = [
        {
            "role": "system",
            "content": "You are a converstion bot"
        },
]

#while in the while, keeps the converstation going until the user enters one of the exit commands
while True:
    User_Input = input(f"\033[1m{username}:\033[0m    ")
    
    #EXIT COMMANDS
    if User_Input in ["Leave", "Exit", "Stop", "Goodbye"]:
        print("you have killed Groq!")
        break
    
    #adds users message to the conversation history
    messages.append(
        {
            "role": "user",
            "content": User_Input
        }
        )


    #this sends conversation history to Groqs API
    stream = client.chat.completions.create(
        
        messages = messages,
        model = "llama-3.3-70b-versatile",
        stream = True
        
    )

    print("\033[1mGroq:\033[0m", end=" ")
    #to collect the full reply from the AI as it streams in
    full_reply = "" 

    for chunk in stream:
        #get the new part of the AI's response
        reply = chunk.choices[0].delta.content

        #if there's content, print and save it
        if reply:
            print(reply, end="", flush=True)
            full_reply += reply
    print()
                
    #adds the full reply to the conversation history (append) keeping the context of the conversation for the next reply
    messages.append({
            "role": "system",
            "content": full_reply
        })


