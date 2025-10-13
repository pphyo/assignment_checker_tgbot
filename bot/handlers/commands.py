import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from bot.config import ASSIGNMENTS
from bot.utils.file_manager import get_user_data_path
import csv

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!\n\nThis is Codoverse.\n\nType /assignments to see the assignment list, or /myresults to check your history.")

async def assignments_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not ASSIGNMENTS:
        await update.message.reply_text("There are currently no assignments available.")
        return
    message = "📄 **Available Assignments:**\n\n"
    for key, data in ASSIGNMENTS.items():
        message += f"🔹 **{data['name']}** (ID: `{key}`)\n"
    message += "\nTo view details, use the `/view <ID>` command.\nExample: `/view roman_to_integer`"
    await update.message.reply_text(message, parse_mode='Markdown')

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