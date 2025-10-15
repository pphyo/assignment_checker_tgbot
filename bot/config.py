import os
import json
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSIGNMENTS_CONFIG_FILE = os.path.join(PROJECT_ROOT, "assignments.json")
USERS_DIR = os.path.join(PROJECT_ROOT, "users")

ASSIGNMENTS = {}

def load_assignments():
    """Load assignments from the global JSON config file into the global ASSIGNMENTS dict."""
    global ASSIGNMENTS
    print(f"Loading assignments from '{ASSIGNMENTS_CONFIG_FILE}'...")
    if not os.path.exists(ASSIGNMENTS_CONFIG_FILE):
        print(f"  - [ERROR] Global config file '{ASSIGNMENTS_CONFIG_FILE}' not found.")
        ASSIGNMENTS.clear()
        return

    try:
        with open(ASSIGNMENTS_CONFIG_FILE, 'r') as f:
            ASSIGNMENTS.update(json.load(f))
        print("  - Successfully loaded and parsed the config file.")
    except Exception as e:
        print(f"  - [ERROR] Failed to load assignments: {e}")
        ASSIGNMENTS.clear()