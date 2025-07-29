from prompt import prompt
# task[user] = list of all tasks assigned to user
tasks = []

# role[user] = role of user
roles = {"hari": "manager"}

# users
users = set()

event_logs = []
maintenance = []
default_durations = []
changes = []
log = []
summary = []

conversations = {}

# system prompt

system_prompt = {
    "role": "system",
    "content": prompt
}


