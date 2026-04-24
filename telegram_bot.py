from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Send me a photo or a message, and I'll forward it.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    target_username = "@pauldatabase"

    await context.bot.send_message(chat_id=target_username, text=text)

    await update.message.reply_text("Your message has been sent!\nMade by @rophy_g")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo = update.message.photo[-1] 
    file = await photo.get_file()

    target_username = "@pauldatabase"  

    await context.bot.send_photo(chat_id=target_username, photo=file.file_id)

    await update.message.reply_text("Your photo has been sent!\nMade by @rophy_g")

def main() -> None:
    TOKEN = os.environ.get("BOT_TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    application.run_polling()

if __name__ == "__main__":
    main()