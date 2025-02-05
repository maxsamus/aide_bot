import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN
from handlers.start_handler import start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    # Create a bot
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Messages
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Run
    application.run_polling()
