```
  ____                    ____ _           _     ____        _   
 / ___|_ __ ___   __ _   / ___| |__   __ _| |_  | __ )  ___ | |_ 
| |  _| '__/ _ \ / _` | | |   | '_ \ / _` | __| |  _ \ / _ \| __|
| |_| | | | (_) | (_| | | |___| | | | (_| | |_  | |_) | (_) | |_ 
 \____|_|  \___/ \__, |  \____|_| |_|\__,_|\__| |____/ \___/ \__|
                    |_|                                          
```
-----------------------------------
# I N T R O

This is a simple Python chatbot using the Groq AI API.
The chatbot maintains a conversation with the user until the user enters a exit command

## Features

- Streams AI replies in real-time to the user
- Keeps the context of the chat to provide a realistic feeling conversation
- Uses exit commands to leave the chat without hassle
- uses a .env file to securely store your Groq AI API key

## Requirements

- 'Groq' package
- 'Python-dotenv' package

you can install these packages with:

`C: > pip install groq`

`C: > pip install python-dotenv`

-----------------------------------
# S E T U P

- Copy the code files
-Create a .env.txt file in the project directory
- add your Groq AI API key to the .env.txt file
           GROQ_API_KEY = Your Api Key
- Run the script!

-----------------------------------
# U S A G E
 
- You will first be asked for your name
- once your name is entered, you can freely chat with Groq until one of the exit commands are entered (Leave, Stop, Exit, or Goodbye)

-----------------------------------
Author: Michelle Thomson

Date: 14/06/25


