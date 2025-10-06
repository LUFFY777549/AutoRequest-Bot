from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler
from Auto.db import add_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await add_user(user.id)

    keyboard = [
        [InlineKeyboardButton("➕ ADD ME TO YOUR CHANNEL", url="https://t.me/AlphaXRequestBot?startchannel=true")],
        [InlineKeyboardButton("➕ ADD ME TO YOUR GROUP", url="https://t.me/AlphaXRequestBot
?startgroup=true")]
    ]

    await update.message.reply_photo(
        "https://files.catbox.moe/1vkwk6.jpg",
        caption=(
            f"Hey {user.mention_html()} 💖,\n\n"
            "I'm <b>Auto Request Approver Bot 🤖!</b>\n"
            "I can approve new join requests in chats.\n"
            "Just add me to the chat with <b>invite users permission</b>.\n\n"
            "Use the button below to add me 👇"
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def register(application):
    application.add_handler(CommandHandler("start", start))