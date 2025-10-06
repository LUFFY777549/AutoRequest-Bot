import logging
from telegram.ext import Application
from Auto.Modules import start, help, bcast, autoapprove, approve

# --- Bot Token (Direct) ---
BOT_TOKEN = "8413484183:AAF11DTGq1aLt37NbbR84e1AXqmBSyJ53RU"

# --- Logging Config ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Register all modules
    start.register(application)
    help.register(application)
    bcast.register(application)
    autoapprove.register(application)
    approve.register(application)

    print("🤖 Auto Request Approver Bot Started Successfully!")
    application.run_polling()

if __name__ == "__main__":
    main()