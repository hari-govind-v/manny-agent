from constants import roles

def upsert_user_profile(name: str, role: str) -> str:
    res = ""
    if name not in roles: 
        res += "User profile created. " 
    roles[name] = role
    res += f"Hello {name}, you are logged in as a {role}!\n"
    return res

upsert_user_profile_schema = {
    "name": "upsert_user_profile",
    "description": "create or update the user profile.",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "User's name"},
            "role": {"type": "string", "description": "User's role"},
        },
        "required": ["name", "role"]
    }
}