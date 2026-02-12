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
    """Load ALL assignments (Active & Inactive) so Admin can manage them."""
    global ASSIGNMENTS
    print(f"Loading assignments from '{ASSIGNMENTS_CONFIG_FILE}'...")
    ASSIGNMENTS.clear()

    if not os.path.exists(ASSIGNMENTS_CONFIG_FILE):
        print(f"  - [ERROR] File not found.")
        return

    try:
        with open(ASSIGNMENTS_CONFIG_FILE, 'r') as f:
            all_data = json.load(f)

        # ⚠️ အရင်ကလို if active: ဆိုပြီး မစစ်တော့ပါဘူး။
        # Admin က အကုန်မြင်ရဖို့ အကုန်ထည့်လိုက်ပါမယ်။
        ASSIGNMENTS.update(all_data) 

        print(f"  - Successfully loaded {len(ASSIGNMENTS)} assignments (Active & Inactive).")

    except Exception as e:
        print(f"  - [ERROR] Failed to load assignments: {e}")
        ASSIGNMENTS.clear()

def save_assignments():
    """Saves the current in-memory ASSIGNMENTS to the JSON file."""
    try:
        with open(ASSIGNMENTS_CONFIG_FILE, 'w') as f:
            json.dump(ASSIGNMENTS, f, indent=4)
        print("✅ Assignments configuration saved to disk.")
        # Reload to ensure consistency
        load_assignments()
    except Exception as e:
        print(f"❌ Failed to save assignments: {e}")