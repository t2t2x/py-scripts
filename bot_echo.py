from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = "6996268577:AAEKSfeq65Z6Zvo_JQsThy9c8LT5e-UE5XI"

async def start(update: Update, context):
    await update.message.reply_text("Hello! This bot simply echos back whatever you type... ")

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

if __name__ == '__main__':
    
    
    app.BotDescription("This is a test for the bot description")

    # Command handlers
    app.add_handler(CommandHandler('start', start))

    # Message handlers
    app.add_handler(MessageHandler(filters.TEXT, echo))

    print("Bot started...")
    app.run_polling()
