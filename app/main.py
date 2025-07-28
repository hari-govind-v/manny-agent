from fastapi import FastAPI
import os
from dotenv import load_dotenv
from agent import run_agent

app = FastAPI()

OPEN_API_KEY = os.getenv("OPEN_API_KEY")

# @app.get("/chat")
# async def agent_manny():
#     pass

if __name__=='__main__':

    # load_dotenv()

    # client = OpenAI(api_key=OPEN_API_KEY)

    # response = client.responses.create(
    #     model="gpt-4o-mini",
    #     input="Write a welcome message to welcome a user Hari to the app."
    # )

    # print(response.output_text)

    user = str(input("What is your name?"))
    prompt = str(input("Enter your prompt : "))

    response = run_agent(prompt, user)
    print(response)

    