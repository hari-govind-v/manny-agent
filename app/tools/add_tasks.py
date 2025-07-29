from constants import tasks

def add_task(task: str, assignee: str) -> str:
    if assignee in tasks:
        try: tasks[assignee].append(task)
        except KeyError: tasks[assignee] = [task]
    print(f"Task added : {task} assigned to {assignee}")
    return f"Task has been assiged to {assignee}"

add_task_schema = {
    "name": "add_task",
    "description": "Add a task and assign it to given user",
    "parameters": {
        "type": "object",
        "properties": {
            "task": {"type": "string", "description": "The task to be done"},
            "assignee": {"type": "string", "description": "The person responsible"},
        },
        "required": ["task", "assignee"],
    },
}
