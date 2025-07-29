from constants import tasks

def get_tasks(user: str):
    if user in tasks:
        return tasks[user]
    else:
        return []
    

get_tasks_schema = {
    "name": "get_tasks",
    "description": "Fetch all tasks of given user",
    "parameters": {
        "type": "object",
        "properties": {
            "user": {"type": "string", "description": "The person responsible"},
        },
        "required": ["user"],
    },
}