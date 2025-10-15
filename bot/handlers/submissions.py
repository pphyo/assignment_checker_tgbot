import os
import shutil
import uuid
import subprocess
from telegram import Update
from telegram.ext import ContextTypes

from bot import config
from bot.utils.file_manager import get_user_data_path, initialize_user_csv, log_submission
from bot.core.runner import run_in_docker

async def handle_submission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.document or not update.message.reply_to_message:
        await update.message.reply_text("Please submit your file by replying to an assignment message.")
        return

    reply_text = update.message.reply_to_message.text
    assignment_id, lang_key = None, None
    last_line = reply_text.splitlines()[-1].strip() if reply_text else ""
    fingerprint_line = last_line.strip('`')

    if fingerprint_line.startswith("ID:"):
        try:
            parts = [part.strip() for part in fingerprint_line.split(':')]
            if len(parts) == 3 and parts[0] == "ID":
                assignment_id, lang_key = parts[1], parts[2]
        except Exception: pass

    if not assignment_id or not lang_key or assignment_id not in config.ASSIGNMENTS or lang_key not in config.ASSIGNMENTS[assignment_id]["languages"]:
        await update.message.reply_text("You did not reply to a valid submission message.")
        return

    assignment = config.ASSIGNMENTS[assignment_id]
    lang_data = assignment["languages"][lang_key]
    submitted_file_name = update.message.document.file_name

    if submitted_file_name != lang_data["file_name"]:
        await update.message.reply_text(f"Incorrect filename. The file must be named `{lang_data['file_name']}`.")
        return

    user_path = get_user_data_path(update)
    initialize_user_csv(user_path)
    processing_message = await update.message.reply_text(f"Received `{submitted_file_name}`. Now checking...", parse_mode='Markdown')
    submission_path = os.path.join(user_path, f"submission_{uuid.uuid4()}")
    os.makedirs(submission_path)

    try:
        await (await context.bot.get_file(update.message.document.file_id)).download_to_drive(custom_path=os.path.join(submission_path, submitted_file_name))
        shutil.copy(lang_data["test_runner"], submission_path)

        final_output, passed_count, total_tests, is_compile_error = final_output, passed_count, total_tests, is_compile_error = run_in_docker(
            docker_image=lang_data["docker_image"],
            host_submission_path=os.path.abspath(submission_path),
            lang_data=lang_data
        )

        if is_compile_error:
            log_submission(user_path, assignment['name'], lang_key, "❌ Compile Error", "0/0")
            await processing_message.edit_text(f"📝 **{assignment['name']} - Compile Error**\n\n```\n{final_output}\n```", parse_mode='Markdown')
            return

        status = "✅ Pass" if passed_count == total_tests and total_tests > 0 else "❌ Fail"
        score = f"{passed_count}/{total_tests}"
        log_submission(user_path, assignment['name'], lang_key, status, score)
        await processing_message.edit_text(f"📝 **{assignment['name']} ({lang_key.capitalize()}) - Test Results**\n\n```\n{final_output}\n```", parse_mode='Markdown')

    except subprocess.TimeoutExpired:
        await processing_message.edit_text("Execution timed out. Your code may have an infinite loop.")
    except Exception as e:
        await processing_message.edit_text(f"An unexpected error occurred: {e}")
    finally:
        if os.path.exists(submission_path): shutil.rmtree(submission_path)