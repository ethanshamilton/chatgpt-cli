# """
# GPT Connection
# Ethan Hamilton -- 04/09/2023
# The purpose of this script is to connect to OpenAI's GPT-4
# through a command line application. 
# """

import os
from dotenv import load_dotenv 
import openai
import requests
import json

# get API key
load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = openai_api_key

headers = {
    "Authorization": f"Bearer {openai_api_key}",
    "Content-Type": "application/json"
}

api_url = "https://api.openai.com/v1/chat/completions"

def chat(messages):
    """
    Send a prompt to GPT and get a response
    prompt: str
    messages: list of dictionaries
    response: str
    """
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages,
        temperature=0.7,
    )
    response = response.choices[0].message['content']
    return response

# set up the application
if __name__ == "__main__":
    print("Welcome to GPT-4 Chatbot CLI!")
    messages = []
    while True:
        user_input = input("\nYou: ")
        messages.append({"role":"user", "content":user_input})
        if user_input.lower() in ["quit", "exit"]:
            break
        response = chat(messages)
        if response:
            print("\nGPT-4: ", response)
            # add the response to a new message object
            messages.append({"role":"assistant", "content":response})
