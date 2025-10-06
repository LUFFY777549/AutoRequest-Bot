from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from Auto.db import set_approval, get_approval

async def approval(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        return await update.message.reply_text("Usage in private chat: /approval [chat_id] on|off")

    chat_id = int(context.args[0])
    mode = context.args[1].lower()

    member = None
    try:
        member = await context.bot.get_chat_member(chat_id, update.effective_user.id)
    except Exception:
        return await update.message.reply_text("Couldn't verify admin status...plz give me admin in your channel/group")

    if not member.can_invite_users:
        return await update.message.reply_text("Couldn't verify admin status...plz give me admin in your channel/group")

    if mode == "on":
        await set_approval(chat_id, True)
        await update.message.reply_text(f"✅ Auto approval enabled for chat ID {chat_id}")
    elif mode == "off":
        await set_approval(chat_id, False)
        await update.message.reply_text(f"❌ Auto approval disabled for chat ID {chat_id}")
    else:
        await update.message.reply_text("Usage in private chat: /approval [chat_id] on|off")

async def checkapproval(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        return await update.message.reply_text("Usage in private: /checkapproval [chat_id]")

    chat_id = int(context.args[0])
    status = await get_approval(chat_id)
    if status:
        await update.message.reply_text(f"✅ Approval is enabled for chat ID {chat_id}")
    else:
        await update.message.reply_text(f"❌ Approval is disabled for chat ID {chat_id}")

async def approveall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        return await update.message.reply_text("Usage: /approveall [chat_id]")
    chat_id = int(context.args[0])
    try:
        requests = await context.bot.get_chat_join_requests(chat_id)
        count = 0
        for req in requests:
            await context.bot.approve_chat_join_request(chat_id, req.from_user.id)
            count += 1
        await update.message.reply_text(f"✅ Successfully approved {count} users in {chat_id}")
    except Exception as e:
        await update.message.reply_text(str(e))

def register(application):
    application.add_handler(CommandHandler("approval", approval))
    application.add_handler(CommandHandler("checkapproval", checkapproval))
    application.add_handler(CommandHandler("approveall", approveall))