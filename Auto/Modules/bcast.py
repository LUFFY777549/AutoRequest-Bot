from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from Auto.db import get_all_users

ADMIN_ID = 7576729648  # your Telegram ID

async def bcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if len(context.args) < 1:
        return await update.message.reply_text("Usage: /bcast [message]")

    text = " ".join(context.args)
    users = await get_all_users()
    sent = 0

    for uid in users:
        try:
            await context.bot.send_message(uid, text)
            sent += 1
        except:
            pass

    await update.message.reply_text(f"✅ Broadcast sent to {sent} users.")

def register(application):
    application.add_handler(CommandHandler("bcast", bcast))