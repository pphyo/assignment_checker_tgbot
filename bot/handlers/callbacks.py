import os
from telegram import Update
from telegram.ext import ContextTypes

from bot.config import ASSIGNMENTS

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