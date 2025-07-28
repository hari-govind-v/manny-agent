from fastapi import FastAPI
import os
from agent import run_agent

app = FastAPI()

OPEN_API_KEY = os.getenv("OPEN_API_KEY")

if __name__=='__main__':

    user = str(input("What is your name?"))
    prompt = str(input("Enter your prompt : "))

    response = run_agent(prompt, user)
    print(response)

    