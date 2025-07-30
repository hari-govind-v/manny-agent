# test_client.py
import requests

API_URL = "http://127.0.0.1:8000/chat"

def print_message(sender, message):
    print(f"({sender}) {message}")

if __name__ == "__main__":
    print("Type 'quit' to exit the chat.")

    user = ""
    role = ""

    while True:
        msg = input("\n> ").strip()
        if msg.lower() == "quit":
            print_message("Manny", "Goodbye!\n\n")
            break

        res = requests.post(
            API_URL, 
            json={
                "message": msg,
                "name":user, 
                "role":role
            })
        
        if res.status_code == 200:
            data = res.json()
            print_message("Manny", data["response"])
        else:
            print("Error:", res.status_code, res.text)
