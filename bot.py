from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

BOT_TOKEN = "PUT_YOUR_TOKEN_HERE"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text
        await update.message.reply_text(f"📩 I received:\n\n{text}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("PapadakhsBot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
