# app/agent.py
from openai import OpenAI
import os
from tools.add_tasks import add_task, add_task_schema
from contants import conversations
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

add_tasks_tool = {
    "type": "function",
    "function": add_task_schema
}

def run_agent(prompt: str, user: str) -> str:

    if user not in conversations:
        conversations[user] = [
            {"role": "system", "content": f"You are Manny, a helpful assistant that manages tasks for user {user}. Always use available tools to respond when a task is mentioned."}
        ]
   
    conversations[user].append({"role": "user", "content": prompt})
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=conversations[user],
        tools=[add_tasks_tool],
        tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:
        for tool_call in message.tool_calls:
            if tool_call.function.name == "add_task":
                args = eval(tool_call.function.arguments)
                result = add_task(**args)
                conversations[user].append({"role": "assistant", "content": result})
                return result
            
    else: print("NO TOOL CALLED")
            
    conversations[user].append({"role": "assistant", "content": message.content})
    return message.content or "No response"
