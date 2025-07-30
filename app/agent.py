import json
from openai import OpenAI
import os
from dotenv import load_dotenv
from constants import conversations, system_prompt
from tools.tools import tools, tools_map

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
ANONYMOUS_ID = "__anonymous__"

def run_agent(
    user_message: str, 
    user: str = "", 
    user_role: str = ""
) -> tuple[str, str | None, str | None]:
    
    if not user: 
        user = ANONYMOUS_ID
    if user not in conversations:
        conversations[user] = [system_prompt]

    if user and user_role:
        user_message = f"{user_role} {user} says '{user_message}'" 

    conversations[user].append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-4",  
        messages=conversations[user],
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message
    result = ""

    if message.tool_calls:
        tool_call_messages = []
        
        for tool_call in message.tool_calls:
            fname = tool_call.function.name
            print(f"\n (LOG) {fname} called. \n")
            args = json.loads(tool_call.function.arguments)

            result = tools_map[fname](**args)

            tool_msg = {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": fname,
                "content": str(result),  
            }
            tool_call_messages.append(tool_msg)

            if fname == "upsert_user_profile":
                user = args["name"]
                user_role = args["role"]
                conversations[user] = conversations.pop(ANONYMOUS_ID)
                conversations[user][0]["content"] += f"\n\nYou are currently assisting **{user}**, who is a **{user_role}**."

        conversations[user].append({
            "role": "assistant",
            "content": None,
            "tool_calls": message.tool_calls
        })
        conversations[user].extend(tool_call_messages)

        followup_response = client.chat.completions.create(
            model="gpt-4",
            messages=conversations[user],
            tools=tools,
            tool_choice="auto"
        )

        followup_msg = followup_response.choices[0].message
        conversations[user].append({
            "role": followup_msg.role,
            "content": followup_msg.content
        })

        result = followup_msg.content
    
    else:  
        result = message.content
        conversations[user].append({
            "role": message.role,
            "content": result,
        })

    return result, user, user_role