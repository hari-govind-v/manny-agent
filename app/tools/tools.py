from .add_tasks import *
from .get_tasks import *
from .upsert_user_profile import *
from .get_user_profile import *

tools_map = {
    "add_task": add_task,
    "get_tasks": get_tasks,
    "upsert_user_profile": upsert_user_profile,
}

tools = [
    {
        "type": "function",
        "function": add_task_schema
    },
    {
        "type": "function",
        "function": get_tasks_schema
    },
    {
        "type": "function",
        "function": upsert_user_profile_schema
    },
    {
        "type": "function",
        "function": get_user_profile_schema
    }
]
