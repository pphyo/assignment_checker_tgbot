import os
import subprocess
import csv
import uuid
import shutil
import json
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN: print("[CRITICAL] BOT_TOKEN not found. Exiting."); exit(1)

ASSIGNMENTS_CONFIG_FILE = "assignments.json"
USERS_DIR = "users"

ASSIGNMENTS = {}

def load_assignments():
    print(f"Loading assignments from '{ASSIGNMENTS_CONFIG_FILE}'...")

    if not os.path.exists(ASSIGNMENTS_CONFIG_FILE): return {}

    try:
        with open(ASSIGNMENTS_CONFIG_FILE, 'r') as f: loaded_assignments = json.load(f)
        print("  - Successfully loaded config file.")
        return loaded_assignments
    except Exception as e:
        print(f"  - [ERROR] Failed to load assignments: {e}")
        return {}

def get_user_data_path(update: Update):
    user = update.effective_user
    user_identifier = user.username if user.username else str(user.id)
    path = os.path.join(USERS_DIR, user_identifier)
    os.makedirs(path, exist_ok=True)
    return path

def initialize_user_csv(user_path):
    csv_path = os.path.join(user_path, "submissions.csv")
    if not os.path.exists(csv_path):
        with open(csv_path, mode='w', newline='') as f: writer = csv.writer(f); writer.writerow(["Timestamp", "Assignment", "Language", "Status", "Score"])

def log_submission(user_path, assignment_name, language, status, score):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S"); csv_path = os.path.join(user_path, "submissions.csv")
    with open(csv_path, mode='a', newline='') as f: writer = csv.writer(f); writer.writerow([timestamp, assignment_name, language, status, score])

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!\n\nThis is Codoverse.\n\nType /assignments to see the assignment list, or /myresults to check your history.")

async def assignments_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not ASSIGNMENTS: await update.message.reply_text("There are currently no assignments available."); return
    message = "📄 **Available Assignments:**\n\n"; [message := message + f"🔹 **{data['name']}** (ID: `{key}`)\n" for key, data in ASSIGNMENTS.items()]
    message += "\nTo view details, use the `/view <ID>` command.\nExample: `/view roman_to_integer`"
    await update.message.reply_text(message, parse_mode='Markdown')

async def view_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args: await update.message.reply_text("Please provide an assignment ID. Example: `/view roman_to_integer`"); return

    assignment_id = context.args[0]
    if assignment_id not in ASSIGNMENTS: await update.message.reply_text(f"Assignment with ID '{assignment_id}' not found."); return

    assignment = ASSIGNMENTS[assignment_id]; description_path = assignment.get("description_file")
    if not description_path or not os.path.exists(description_path): await update.message.reply_text("Sorry, a detailed description is not available for this assignment."); return

    with open(description_path, 'r', encoding='utf-8') as f: description_text = f.read()
    await update.message.reply_text(description_text, parse_mode='Markdown')

    keyboard = []
    for lang_key, lang_data in assignment.get("languages", {}).items():
        keyboard.append([InlineKeyboardButton(lang_key.capitalize(), callback_data=f"lang_select:{assignment_id}:{lang_key}")])

    if keyboard:
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('Please choose your programming language:', reply_markup=reply_markup)

async def language_choice_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    action, assignment_id, lang_key = query.data.split(':')
    assignment = ASSIGNMENTS[assignment_id]
    lang_data = assignment["languages"][lang_key]
    template_path = lang_data.get("template_file")

    if not template_path or not os.path.exists(template_path):
        await query.edit_message_text(text=f"Sorry, the code template for {lang_key.capitalize()} is missing.")
        return

    with open(template_path, 'r', encoding='utf-8') as f:
        template_code = f.read()

    await query.edit_message_text(text=f"You have selected: *{lang_key.capitalize()}*.\n\nHere is your code template:", parse_mode='Markdown')

    await context.bot.send_message(
        chat_id=query.message.chat_id,
        text=f"```\n{template_code}\n```",
        parse_mode='Markdown'
    )

    fingerprint = f"ID:{assignment_id}:{lang_key}"

    await context.bot.send_message(
        chat_id=query.message.chat_id,
        text=f"To submit for **{assignment['name']} ({lang_key.capitalize()})**, reply to this message with your `{lang_data['file_name']}` file.\n\n`{fingerprint}`",
        parse_mode='Markdown'
    )

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
        await update.message.reply_text("Please submit your file by replying to an assignment message.\nUse `/view <assignment_id>` to get the correct message to reply to.")
        return

    reply_text = update.message.reply_to_message.text

    assignment_id, lang_key = None, None
    last_line = reply_text.splitlines()[-1].strip() if reply_text else ""

    if last_line.startswith("ID:"):
        try:
            parts = last_line.split(':')
            if len(parts) == 3 and parts[0] == "ID":
                assignment_id = parts[1]
                lang_key = parts[2]
        except Exception:
            pass

    if not assignment_id or not lang_key or assignment_id not in ASSIGNMENTS or lang_key not in ASSIGNMENTS[assignment_id]["languages"]:
        await update.message.reply_text("You did not reply to a valid assignment submission message. Please use the `/view` command and choose a language first.")
        return

    assignment = ASSIGNMENTS[assignment_id]
    lang_data = assignment["languages"][lang_key]
    submitted_file_name = update.message.document.file_name


    if submitted_file_name != lang_data["file_name"]:
        await update.message.reply_text(f"Incorrect filename. The file must be named `{lang_data['file_name']}`.")
        return

    user_path = get_user_data_path(update)
    initialize_user_csv(user_path)
    processing_message = await update.message.reply_text(f"Received `{submitted_file_name}`. Now checking for `{assignment['name']}`...", parse_mode='Markdown')
    submission_path = os.path.join(user_path, f"submission_{uuid.uuid4()}"); os.makedirs(submission_path)

    try:
        await (await context.bot.get_file(update.message.document.file_id)).download_to_drive(custom_path=os.path.join(submission_path, submitted_file_name))
        shutil.copy(lang_data["test_runner"], submission_path)

        host_submission_path = os.path.abspath(submission_path)
        container_work_dir = "/app"
        docker_image = lang_data["docker_image"]
        runner_file = os.path.basename(lang_data["test_runner"])

        command_to_run = ""

        if lang_key == "java":
            runner_class_name = runner_file.replace(".java", "")
            command_to_run = f"javac *.java && java {runner_class_name}"
        elif lang_key == "python":
            command_to_run = f"python3 {runner_file}"

        docker_command = ["docker", "run", "--rm", "--network", "none", "-v", f"{host_submission_path}:{container_work_dir}", "--workdir", container_work_dir, docker_image, "sh", "-c", command_to_run]
        run_process = subprocess.run(docker_command, capture_output=True, text=True, timeout=20)

        final_output = run_process.stdout + run_process.stderr
        passed_count, total_tests = 0, 0
        is_compile_error = (lang_key == "java" and "error:" in run_process.stderr and "[SUMMARY]:" not in run_process.stdout)

        if is_compile_error:
            log_submission(user_path, assignment['name'], lang_key, "❌ Compile Error", "0/0")
            await processing_message.edit_text(f"📝 **{assignment['name']} - Compile Error**\n\n```\n{run_process.stderr}\n```", parse_mode='Markdown')
            return

        for line in run_process.stdout.splitlines():
            if line.startswith("[SUMMARY]:"):
                parts = line.strip().split(':'); passed_count, total_tests = int(parts[1]), int(parts[2])
        status = "✅ Pass" if passed_count == total_tests and total_tests > 0 else "❌ Fail"
        score = f"{passed_count}/{total_tests}"
        log_submission(user_path, assignment['name'], lang_key, status, score)
        await processing_message.edit_text(f"📝 **{assignment['name']} ({lang_key.capitalize()}) - Test Results**\n\n```\n{final_output}\n```", parse_mode='Markdown')

    except Exception as e:
        await processing_message.edit_text(f"An unexpected error occurred: {e}")
    finally:
        if os.path.exists(submission_path): shutil.rmtree(submission_path)

async def post_init(application: Application):
    print("Setting up bot commands..."); bot_commands = [BotCommand("start", "Start the bot"), BotCommand("assignments", "List assignments"), BotCommand("view", "View assignment details"), BotCommand("myresults", "Check your history")]
    await application.bot.set_my_commands(bot_commands); print("Bot commands set successfully.")

def main():
    global ASSIGNMENTS; ASSIGNMENTS = load_assignments()

    if not ASSIGNMENTS: print("[CRITICAL] No assignments found.")
    os.makedirs(USERS_DIR, exist_ok=True)

    print("Building application...")

    application = Application.builder().token(BOT_TOKEN).post_init(post_init).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("assignments", assignments_command))
    application.add_handler(CommandHandler("view", view_command))
    application.add_handler(CommandHandler("myresults", myresults_command))
    application.add_handler(CallbackQueryHandler(language_choice_callback))
    application.add_handler(MessageHandler(filters.Document.ALL & filters.REPLY, handle_submission))
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command_handler))

    print("Bot starting polling...")
    application.run_polling()

if __name__ == "__main__":
    main()