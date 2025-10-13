import os
import subprocess
import csv
import uuid
import shutil
import json
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

ASSIGNMENTS_CONFIG_FILE = "assignments.json"
BOT_TOKEN = os.getenv("BOT_TOKEN")
USERS_DIR = "users"
DOCKER_IMAGE_NAME = "assignment-checker-env"

if not BOT_TOKEN:
    print("[CRITICAL] BOT_TOKEN not found in .env file or environment variables. Exiting.")
    exit(1)

ASSIGNMENTS = {}

def load_assignments():
    """Load assignments from a single global JSON config file."""
    print(f"Loading assignments from '{ASSIGNMENTS_CONFIG_FILE}'...")
    if not os.path.exists(ASSIGNMENTS_CONFIG_FILE):
        print(f"  - [ERROR] Global config file '{ASSIGNMENTS_CONFIG_FILE}' not found.")
        return {}
    try:
        with open(ASSIGNMENTS_CONFIG_FILE, 'r') as f:
            loaded_assignments = json.load(f)
            print("  - Successfully loaded and parsed the config file.")
            for key, data in loaded_assignments.items():
                if not os.path.exists(data['test_runner']):
                     print(f"    - [WARNING] Test runner not found for '{key}': {data['test_runner']}")
                else:
                    print(f"    - Found assignment: {data['name']}")
            return loaded_assignments
    except json.JSONDecodeError:
        print(f"  - [ERROR] Invalid JSON format in '{ASSIGNMENTS_CONFIG_FILE}'. Please check the file content.")
        return {}
    except Exception as e:
        print(f"  - [ERROR] An unexpected error occurred while loading assignments: {e}")
        return {}

def get_user_data_path(update: Update):
    """Get the unique data path for a user."""
    user = update.message.from_user
    user_identifier = user.username if user.username else str(user.id)
    path = os.path.join(USERS_DIR, user_identifier)
    os.makedirs(path, exist_ok=True)
    return path

def initialize_user_csv(user_path):
    """Initialize a CSV file for a specific user if it doesn't exist."""
    csv_path = os.path.join(user_path, "submissions.csv")
    if not os.path.exists(csv_path):
        with open(csv_path, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Assignment", "Status", "Score"])

def log_submission(user_path, assignment_name, status, score):
    """Log a submission to the user's personal CSV file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    csv_path = os.path.join(user_path, "submissions.csv")
    with open(csv_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, assignment_name, status, score])

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!\n\nThis is Codoverse.\n\nType /assignments to see the assignment list, or /myresults to check your history.")

async def assignments_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not ASSIGNMENTS:
        await update.message.reply_text("There are currently no assignments available.")
        return
    message = "📄 **Available Assignments:**\n\n"
    for key, data in ASSIGNMENTS.items():
        message += f"🔹 **{data['name']}** (ID: `{key}`)\n"
        message += f"   - Required file: `{data['file_name']}`\n\n"
    message += "To view details, use the `/view <ID>` command.\nExample: `/view roman_to_integer`"
    await update.message.reply_text(message, parse_mode='Markdown', disable_web_page_preview=True)

async def view_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide an assignment ID. Example: `/view roman_to_integer`")
        return
    assignment_id = context.args[0]
    if assignment_id not in ASSIGNMENTS:
        await update.message.reply_text(f"Assignment with ID '{assignment_id}' not found.")
        return
    assignment = ASSIGNMENTS[assignment_id]
    description_path = assignment.get("description_file")
    if not description_path or not os.path.exists(description_path):
        await update.message.reply_text("Sorry, a detailed description is not available for this assignment.")
        return
    with open(description_path, 'r', encoding='utf-8') as f:
        description_text = f.read()
    await update.message.reply_text(description_text, parse_mode='Markdown')
    await update.message.reply_text(f"To submit for **{assignment['name']}**, reply to this message.\nID: `{assignment_id}`", parse_mode='Markdown')

async def myresults_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_path = get_user_data_path(update)
    csv_path = os.path.join(user_path, "submissions.csv")
    if not os.path.exists(csv_path):
        await update.message.reply_text("You have no submission records yet.")
        return
    user_results = []
    with open(csv_path, mode='r') as f:
        reader = csv.reader(f)
        try:
            next(reader)
            for row in reader:
                user_results.append(f"🗓️ {row[0]} - {row[1]} - {row[2]} (Score: {row[3]})")
        except StopIteration: pass
    if not user_results:
        await update.message.reply_text("You have no submission records yet.")
    else:
        user_results.reverse()
        await update.message.reply_text("👤 **Your Submission History:**\n\n" + "\n".join(user_results), parse_mode='Markdown')

async def unknown_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sorry, I didn't understand that command. Please use one of the following:\n\n"
        "/start - Start the bot\n"
        "/assignments - List all available assignments\n"
        "/view <ID> - View details of a specific assignment\n"
        "/myresults - Check your submission history"
    )

async def handle_submission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.document or not update.message.reply_to_message:
        await update.message.reply_text("Please reply to an assignment message before sending your Java file.\n\nType /assignments to see the list.")
        return
    reply_text = update.message.reply_to_message.text
    assignment_id = next((key for key in ASSIGNMENTS if f"ID: {key}" in reply_text), None)
    if not assignment_id:
        await update.message.reply_text("You did not reply to a valid assignment message.")
        return

    assignment = ASSIGNMENTS[assignment_id]
    submitted_file_name = update.message.document.file_name
    if submitted_file_name != assignment["file_name"]:
        await update.message.reply_text(f"Incorrect filename. The file must be named `{assignment['file_name']}`.")
        return

    user_path = get_user_data_path(update)
    initialize_user_csv(user_path)
    processing_message = await update.message.reply_text(f"Received `{submitted_file_name}`. Now checking for `{assignment['name']}`...", parse_mode='Markdown')
    submission_path = os.path.join(user_path, f"submission_{uuid.uuid4()}")
    os.makedirs(submission_path)

    try:
        student_file_obj = await context.bot.get_file(update.message.document.file_id)
        await student_file_obj.download_to_drive(custom_path=os.path.join(submission_path, submitted_file_name))
        shutil.copy(assignment["test_runner"], submission_path)

        host_submission_path = os.path.abspath(submission_path)
        container_work_dir = "/app"
        runner_class_name = os.path.basename(assignment["test_runner"]).replace(".java", "")
        command_to_run_in_container = f"javac *.java && java {runner_class_name}"
        docker_command = [
            "docker", "run", "--rm", "--network", "none",
            "-v", f"{host_submission_path}:{container_work_dir}",
            "--workdir", container_work_dir, DOCKER_IMAGE_NAME,
            "sh", "-c", command_to_run_in_container
        ]
        run_process = subprocess.run(docker_command, capture_output=True, text=True, timeout=20)

        if "error:" in run_process.stderr and "[SUMMARY]:" not in run_process.stdout:
            log_submission(user_path, assignment['name'], "❌ Compile Error", "0/0")
            await processing_message.edit_text(f"📝 **{assignment['name']} - Compile Error**\n\n```\n{run_process.stderr}\n```", parse_mode='Markdown')
            return

        final_output = run_process.stdout + run_process.stderr
        passed_count, total_tests = 0, 0
        for line in run_process.stdout.splitlines():
            if line.startswith("[SUMMARY]:"):
                parts = line.strip().split(':')
                passed_count, total_tests = int(parts[1]), int(parts[2])

        status = "✅ Pass" if passed_count == total_tests and total_tests > 0 else "❌ Fail"
        score = f"{passed_count}/{total_tests}"
        log_submission(user_path, assignment['name'], status, score)

        await processing_message.edit_text(f"📝 **{assignment['name']} - Test Results**\n\n```\n{final_output}\n```", parse_mode='Markdown')

    except subprocess.TimeoutExpired:
        await processing_message.edit_text("Execution timed out. Your code may have an infinite loop.")
    except Exception as e:
        await processing_message.edit_text(f"An unexpected error occurred: {e}")
    finally:
        if os.path.exists(submission_path):
            shutil.rmtree(submission_path)

async def post_init(application: Application):
    """Initializes bot commands after the application is built."""
    print("Setting up bot commands...")
    bot_commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("assignments", "List all available assignments"),
        BotCommand("view", "View details of an assignment (e.g., /view <ID>)"),
        BotCommand("myresults", "Check your submission history")
    ]
    await application.bot.set_my_commands(bot_commands)
    print("Bot commands set successfully.")

def main():
    """Sets up and runs the bot."""
    global ASSIGNMENTS
    ASSIGNMENTS = load_assignments()
    if not ASSIGNMENTS:
        print("[CRITICAL] No assignments found. Please check your 'assignments.json' file.")

    os.makedirs(USERS_DIR, exist_ok=True)

    print("Building application...")

    application = Application.builder().token(BOT_TOKEN).post_init(post_init).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("assignments", assignments_command))
    application.add_handler(CommandHandler("view", view_command))
    application.add_handler(CommandHandler("myresults", myresults_command))
    application.add_handler(MessageHandler(filters.Document.ALL & filters.REPLY, handle_submission))
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command_handler)) # This must be the last handler

    print("Bot starting polling...")
    application.run_polling()

if __name__ == "__main__":
    main()