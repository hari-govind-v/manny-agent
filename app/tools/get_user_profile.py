from constants import roles

def get_user_profile(name: str) -> str:
    role = roles.get(name.lower())
    if role:
        return f"{name} is a {role}."
    return f"No role found for {name}."


get_user_profile_schema = {
    "name": "get_user_profile",
    "description": "Retrieve the role of a user if known.",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "The user's name."
            }
        },
        "required": ["name"]
    }
}

