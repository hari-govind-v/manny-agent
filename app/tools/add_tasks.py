from contants import tasks

def add_task(task: str, assignee: str) -> str:
    tasks.append((task, assignee))
    print(f"Task added : {task} assigned to {assignee}")
    return f"Task has been assiged to {assignee}"

add_task_schema = {
    "name": "add_task",
    "description": "Add a task and assign it to a user",
    "parameters": {
        "type": "object",
        "properties": {
            "task": {"type": "string", "description": "The task to be done"},
            "assignee": {"type": "string", "description": "The person responsible"},
        },
        "required": ["task", "assignee"],
    },
}
