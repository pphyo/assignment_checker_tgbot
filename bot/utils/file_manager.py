import os
import csv
from datetime import datetime
from telegram import Update

from bot.config import USERS_DIR

def get_user_data_path(update: Update):
    """Get the unique data path for a user."""
    user = update.effective_user
    user_identifier = user.username if user.username else str(user.id)
    path = os.path.join(USERS_DIR, user_identifier)
    os.makedirs(path, exist_ok=True)
    return path

def initialize_user_csv(user_path: str):
    """Initialize a CSV file for a specific user if it doesn't exist."""
    csv_path = os.path.join(user_path, "submissions.csv")
    if not os.path.exists(csv_path):
        with open(csv_path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Assignment", "Language", "Status", "Score"])

def log_submission(user_path: str, assignment_name: str, language: str, status: str, score: str):
    """Log a submission to the user's personal CSV file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    csv_path = os.path.join(user_path, "submissions.csv")
    with open(csv_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, assignment_name, language, status, score])