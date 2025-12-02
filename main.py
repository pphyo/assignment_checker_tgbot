import os
from telegram import BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from bot import config
from bot.handlers import commands, callbacks, submissions

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

    config.load_assignments()

    if not config.BOT_TOKEN:
        print("[CRITICAL] BOT_TOKEN not found in .env file. Exiting.")
        return
    if not config.ASSIGNMENTS:
        print("[CRITICAL] No assignments found. Please check 'assignments.json'.")

    os.makedirs(config.USERS_DIR, exist_ok=True)

    print("Building application...")

    application = Application.builder().token(config.BOT_TOKEN).post_init(post_init).build()

    application.add_handler(CommandHandler("start", commands.start_command))
    application.add_handler(CommandHandler("assignments", commands.assignments_command))
    application.add_handler(CommandHandler("view", commands.view_command))
    application.add_handler(CommandHandler("myresults", commands.myresults_command))
    application.add_handler(CommandHandler("reload", commands.reload_command))
    application.add_handler(CommandHandler("export", commands.export_scores_command))
    application.add_handler(CallbackQueryHandler(callbacks.language_choice_callback))
    application.add_handler(MessageHandler(filters.Document.ALL & filters.REPLY, submissions.handle_submission))
    application.add_handler(MessageHandler(filters.COMMAND, commands.unknown_command_handler))

    print("Bot starting polling...")
    application.run_polling()

if __name__ == "__main__":
    main()