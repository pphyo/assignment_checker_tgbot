from datetime import datetime
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from bot.utils.file_manager import compile_all_submissions
from bot import config
from bot.utils.file_manager import get_user_data_path
import csv

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!\n\nThis is Codoverse.\n\nType /assignments to see the assignment list, or /myresults to check your history.")

async def assignments_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Lists ONLY ACTIVE assignments for students."""

    active_list = []
    for key, data in config.ASSIGNMENTS.items():
        if data.get('active', True) is True:
            active_list.append(f"📝 *{key}*: {data['name']}")

    if not active_list:
        await update.message.reply_text("There are currently no active assignments.")
        return

    message = "📚 *Available Assignments:*\n\n" + "\n".join(active_list)
    message += "\n\nUse `/view <id>` to see details."
    await update.message.reply_text(message, parse_mode='Markdown')

async def view_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide an assignment ID. Example: `/view roman_to_integer`")
        return

    assignment_id = context.args[0]
    if assignment_id not in config.ASSIGNMENTS:
        await update.message.reply_text(f"Assignment with ID '{assignment_id}' not found.")
        return

    assignment = config.ASSIGNMENTS[assignment_id]
    description_path = assignment.get("description_file")

    if not description_path or not os.path.exists(description_path):
        await update.message.reply_text("Sorry, a detailed description is not available for this assignment.")
        return

    with open(description_path, 'r', encoding='utf-8') as f:
        description_text = f.read()

    await update.message.reply_text(description_text, parse_mode='Markdown')

    keyboard = [[InlineKeyboardButton(lang_key.capitalize(), callback_data=f"lang_select:{assignment_id}:{lang_key}")] for lang_key in assignment.get("languages", {})]
    if keyboard:
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('Please choose your programming language:', reply_markup=reply_markup)

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
                user_results.append(f"🗓️ {row[0]} - {row[1]} ({row[2]}) - {row[3]} (Score: {row[4]})")
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

async def reload_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Reloads the assignments configuration without restarting the bot."""
    user_id = str(update.effective_user.id)

    print(f"DEBUG: Attempting reload. User ID: {user_id}. Expected Admin ID: {config.ADMIN_ID}")

    if user_id != config.ADMIN_ID:
        await update.message.reply_text("⛔️ Unauthorized. Your ID does not match the Admin ID.")
        return

    config.load_assignments()

    await update.message.reply_text(
        f"✅ Configuration reloaded successfully!\n"
        f"Loaded {len(config.ASSIGNMENTS)} active assignments."
    )

async def export_scores_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin command to download all student scores as a CSV file."""
    user_id = str(update.effective_user.id)

    if user_id != config.ADMIN_ID:
        await update.message.reply_text("⛔️ Unauthorized access.")
        return

    await update.message.reply_text("🔄 Compiling all scores... Please wait.")

    report_file = compile_all_submissions()

    if report_file and os.path.exists(report_file):
        await update.message.reply_document(
            document=open(report_file, 'rb'),
            filename=f"All_Scores_{datetime.now().strftime('%Y%m%d')}.csv",
            caption="📊 Here is the consolidated score report."
        )

        os.remove(report_file)
    else:
        await update.message.reply_text("⚠️ No submission data found yet.")