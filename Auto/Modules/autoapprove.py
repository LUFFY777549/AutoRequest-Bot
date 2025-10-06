from telegram import Update
from telegram.ext import ContextTypes, ChatJoinRequestHandler
from Auto.db import get_approval

async def auto_approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = update.chat_join_request
    chat_id = req.chat.id
    user_id = req.from_user.id

    status = await get_approval(chat_id)
    if not status:
        return

    await context.bot.approve_chat_join_request(chat_id, user_id)
    try:
        owner = (await context.bot.get_chat(chat_id)).owner
        text = f"✅ Successfully approved 1 out of 1 users in {chat_id}"
        await context.bot.send_message(owner.id, text)
    except Exception:
        pass

def register(application):
    application.add_handler(ChatJoinRequestHandler(auto_approve))