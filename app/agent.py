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

    if user not in conversations:
        conversations[user] = [system_prompt]

    if user and user_role:
        user_message = f"{user_role} {user} says '{user_message}'" 

    conversations[user].append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversations[user],
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message
    conversations[user].append(message)

    if message.tool_calls:
        tool_call_messages = []
        name, role = None, None

        for tool_call in message.tool_calls:
            fname = tool_call.function.name
            print(f"\n (LOG) {fname} called. \n")
            args = json.loads(tool_call.function.arguments)

            result = tools_map[fname](**args)

            tool_msg = {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": fname,
                "content": result,
            }
            tool_call_messages.append(tool_msg)

            if fname == "upsert_user_profile":
                name = args["name"]
                role = args["role"]
                conversations[name] = conversations.pop(ANONYMOUS_ID)
                user = name

        conversations[user].extend(tool_call_messages)  # append tool responses

        # Follow up call to prompt user for details
        followup_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversations[user],
            tools=tools,
            tool_choice="auto"
        )

        followup_message = followup_response.choices[0].message
        conversations[user].append({
            "role": "assistant",
            "content": followup_message.content
        })

        return followup_message.content or "No response", name, role

    conversations[user].append({
        "role": "assistant", 
        "content": message.content
    })
    return message.content or "No response", None, None
