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

def compile_all_submissions(output_file="master_report.csv"):
    """
    Walks through all user folders, collects submissions, and writes to a master CSV.
    Returns the path to the created master file or None if no data found.
    """
    all_rows = []

    header = ["UserIdentifier", "Timestamp", "Assignment", "Language", "Status", "Score"]

    if not os.path.exists(USERS_DIR):
        return None

    for user_id in os.listdir(USERS_DIR):
        user_path = os.path.join(USERS_DIR, user_id)

        if os.path.isdir(user_path):
            csv_path = os.path.join(user_path, "submissions.csv")

            if os.path.exists(csv_path):
                try:
                    with open(csv_path, mode='r', encoding='utf-8') as f:
                        reader = csv.reader(f)
                        next(reader, None)

                        for row in reader:
                            all_rows.append([user_id] + row)
                except Exception as e:
                    print(f"[ERROR] Reading CSV for {user_id}: {e}")

    if not all_rows:
        return None

    with open(output_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(all_rows)

    return output_file