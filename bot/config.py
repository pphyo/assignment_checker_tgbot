import os
import json
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSIGNMENTS_CONFIG_FILE = os.path.join(PROJECT_ROOT, "assignments.json")
USERS_DIR = os.path.join(PROJECT_ROOT, "users")

ASSIGNMENTS = {}

def load_assignments():
    """Load ONLY ACTIVE assignments from the global JSON config file."""
    global ASSIGNMENTS
    print(f"Loading assignments from '{ASSIGNMENTS_CONFIG_FILE}'...")
    ASSIGNMENTS.clear()

    if not os.path.exists(ASSIGNMENTS_CONFIG_FILE):
        print(f"  - [ERROR] Global config file '{ASSIGNMENTS_CONFIG_FILE}' not found.")
        return

    try:
        with open(ASSIGNMENTS_CONFIG_FILE, 'r') as f:
            all_assignments_data = json.load(f)

        active_assignments = {}
        for key, data in all_assignments_data.items():

            if data.get("active", True):
                active_assignments[key] = data
                print(f"    - Loaded ACTIVE assignment: {data['name']}")
            else:
                print(f"    - Skipping INACTIVE assignment: {data.get('name', key)}")

        ASSIGNMENTS.update(active_assignments)
        print(f"  - Successfully loaded {len(ASSIGNMENTS)} active assignments.")

    except Exception as e:
        print(f"  - [ERROR] Failed to load assignments: {e}")
        ASSIGNMENTS.clear()