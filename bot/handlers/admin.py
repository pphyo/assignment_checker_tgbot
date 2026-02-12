import os
import glob
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot import config

# --- Feature 1: Toggle Assignments ---

async def admin_panel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Displays a control panel to toggle assignments."""

    # 1. User ID ကို နေရာမှန်ကနေ ယူမယ်
    if update.callback_query:
        user_id = str(update.callback_query.from_user.id)
    else:
        user_id = str(update.effective_user.id)

    if user_id != config.ADMIN_ID:
        return # Ignore non-admins

    # 2. Keyboard တည်ဆောက်မယ်
    keyboard = []
    for key, data in config.ASSIGNMENTS.items():
        is_active = data.get('active', True)
        status_icon = "✅" if is_active else "❌"
        # Callback data format: "toggle_<assignment_id>"
        btn_text = f"{status_icon} {data['name']}"
        keyboard.append([InlineKeyboardButton(btn_text, callback_data=f"toggle_{key}")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "🔧 *Admin Control Panel*\nClick to toggle availability:"

    # 3. Context ပေါ်မူတည်ပြီး ပို့မလား Edit မလား ဆုံးဖြတ်မယ်
    if update.callback_query:
        # Button နှိပ်လို့ ရောက်လာတာဆိုရင် ရှိပြီးသား Message ကိုပဲ ပြင်မယ် (Edit)
        await update.callback_query.message.edit_text(
            text, 
            reply_markup=reply_markup, 
            parse_mode='Markdown'
        )
    else:
        # /admin လို့ ရိုက်လို့ ရောက်လာတာဆိုရင် Message အသစ်ပို့မယ် (Reply)
        await update.message.reply_text(
            text, 
            reply_markup=reply_markup, 
            parse_mode='Markdown'
        )

async def toggle_assignment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the button click to toggle status."""
    query = update.callback_query
    # Button နှိပ်တာကို လက်ခံရရှိကြောင်း အကြောင်းကြားမယ် (loading circle ပျောက်သွားအောင်)
    await query.answer()

    if str(query.from_user.id) != config.ADMIN_ID:
        return

    data = query.data
    if data.startswith("toggle_"):
        assignment_id = data.replace("toggle_", "")

        if assignment_id in config.ASSIGNMENTS:
            # Toggle the boolean
            current_status = config.ASSIGNMENTS[assignment_id].get('active', True)
            config.ASSIGNMENTS[assignment_id]['active'] = not current_status

            # Save to JSON file
            config.save_assignments()

            # Refresh the panel (UI update)
            # ဒီနေရာမှာ update object အဟောင်းကိုပဲ ပြန်သုံးပြီး admin_panel_command ကို ခေါ်လိုက်မယ်
            await admin_panel_command(update, context)
        else:
            await query.edit_message_text("Error: Assignment not found.")

# --- Feature 2: Get Student Code ---

async def get_student_code_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Usage: /getcode <username_or_id> <assignment_id>
    Example: /getcode pphyo roman_to_integer
    """
    user_id = str(update.effective_user.id)
    if user_id != config.ADMIN_ID:
        return

    args = context.args
    if len(args) != 2:
        await update.message.reply_text("Usage: `/getcode <username> <assignment_id>`", parse_mode='Markdown')
        return

    target_user = args[0]
    assignment_id = args[1]

    # Construct path: users/{target_user}/{assignment_id}/submissions/
    base_path = os.path.join(config.USERS_DIR, target_user, assignment_id, "submissions")

    if not os.path.exists(base_path):
        await update.message.reply_text(f"❌ No submissions found for `{target_user}` in `{assignment_id}`.", parse_mode='Markdown')
        return

    # Find the latest file (by name timestamp)
    list_of_files = glob.glob(os.path.join(base_path, "*"))
    if not list_of_files:
        await update.message.reply_text("Folder exists but is empty.")
        return

    latest_file = max(list_of_files, key=os.path.getctime)
    file_name = os.path.basename(latest_file)

    await update.message.reply_document(
        document=open(latest_file, 'rb'),
        filename=file_name,
        caption=f"📄 Latest submission for {target_user} ({assignment_id})"
    )