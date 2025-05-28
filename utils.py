import json
from datetime import datetime

def log_interaction(inquiry, intent, response):
    log = {
        "timestamp": datetime.now().isoformat(),
        "inquiry": inquiry,
        "intent": intent,
        "response": response
    }
    with open("chat_log.json", "a") as f:
        f.write(json.dumps(log) + "\n")