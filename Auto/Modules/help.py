from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "⚡️<b>How To use Auto Request Approval Bot</b>⚡️\n"
        "Tired of manually approving join requests? Let the bot handle it ✨\n\n"
        "Bot - @AutoReqApprover_Bot\n\n"
        "Features:\n"
        " - /approval [chat_id] on|off - Enable/Disable auto-approval\n"
        " - /checkapproval [chat_id] - Check approval mode\n"
        " - /approveall [chat_id] - Approve all pending join requests\n\n"
        "⚠️ <b>Important:</b>\n"
        "Give the bot 'Invite Users via Link' permission!\n\n"
        "🥂 Just add the bot & relax 😌"
    )
    await update.message.reply_text(text, parse_mode="HTML")

def register(application):
    application.add_handler(CommandHandler("help", help_command))