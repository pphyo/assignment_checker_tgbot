import os
import json
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ASSIGNMENTS_CONFIG_FILE = "assignments.json"
USERS_DIR = "users"

ASSIGNMENTS = {}

def load_assignments():
    """Load assignments from the global JSON config file into the global ASSIGNMENTS dict."""
    global ASSIGNMENTS
    print(f"Loading assignments from '{ASSIGNMENTS_CONFIG_FILE}'...")
    if not os.path.exists(ASSIGNMENTS_CONFIG_FILE):
        print(f"  - [ERROR] Global config file '{ASSIGNMENTS_CONFIG_FILE}' not found.")
        ASSIGNMENTS = {}
        return

    try:
        with open(ASSIGNMENTS_CONFIG_FILE, 'r') as f:
            ASSIGNMENTS = json.load(f)
        print("  - Successfully loaded and parsed the config file.")
    except Exception as e:
        print(f"  - [ERROR] Failed to load assignments: {e}")
        ASSIGNMENTS = {}