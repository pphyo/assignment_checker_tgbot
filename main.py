import logging
import os
from telegram import BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from bot import config
from bot.handlers import commands, callbacks, submissions, admin

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def post_init(application: Application):
    """Initializes bot commands menu after the application is built."""
    print("Setting up bot commands...")
    # Admin commands like /admin, /reload, /export are usually hidden from the public menu
    bot_commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("assignments", "List active assignments"),
        BotCommand("view", "View details of an assignment (e.g., /view <ID>)"),
        BotCommand("myresults", "Check your submission history")
    ]
    await application.bot.set_my_commands(bot_commands)
    print("Bot commands set successfully.")

def main():
    """Sets up and runs the bot."""

    # 1. Load Assignments
    config.load_assignments()

    # 2. Validation Checks
    if not config.BOT_TOKEN:
        print("[CRITICAL] BOT_TOKEN not found in .env file. Exiting.")
        return
    if not config.ASSIGNMENTS:
        print("[WARNING] No assignments found (or all are inactive). Please check 'assignments.json'.")

    # 3. Ensure Directories Exist
    os.makedirs(config.USERS_DIR, exist_ok=True)

    print("Building application...")

    # 4. Build Application
    application = Application.builder().token(config.BOT_TOKEN).post_init(post_init).build()

    # --- A. Standard Command Handlers ---
    application.add_handler(CommandHandler("start", commands.start_command))
    application.add_handler(CommandHandler("assignments", commands.assignments_command))
    application.add_handler(CommandHandler("view", commands.view_command))
    application.add_handler(CommandHandler("myresults", commands.myresults_command))

    # --- B. Admin Command Handlers ---
    # Reload config without restarting
    application.add_handler(CommandHandler("reload", commands.reload_command))
    # Export scores to CSV
    application.add_handler(CommandHandler("export", commands.export_scores_command))
    # Show Admin Panel (Toggle Assignments)
    application.add_handler(CommandHandler("admin", admin.admin_panel_command))
    # Get Student Code
    application.add_handler(CommandHandler("getcode", admin.get_student_code_command))

    # --- C. Callback Query Handlers (Button Clicks) ---
    # Important: Specific patterns should come BEFORE generic ones if they might conflict.

    # 1. Admin Toggle Buttons (Matches data starting with "toggle_")
    application.add_handler(CallbackQueryHandler(admin.toggle_assignment_callback, pattern="^toggle_"))

    # 2. Language Selection Buttons (Matches everything else or specific language patterns)
    # Assuming language buttons don't start with "toggle_"
    application.add_handler(CallbackQueryHandler(callbacks.language_choice_callback))

    # --- D. Message Handlers (File Submissions) ---
    # Handles document uploads that are replies to bot messages
    application.add_handler(MessageHandler(filters.Document.ALL & filters.REPLY, submissions.handle_submission))

    # --- E. Fallback Handler ---
    # Handles unknown commands (Should be last)
    application.add_handler(MessageHandler(filters.COMMAND, commands.unknown_command_handler))

    print("Bot starting polling...")
    application.run_polling()

if __name__ == "__main__":
    main()