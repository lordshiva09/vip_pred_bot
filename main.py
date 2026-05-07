import traceback
from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN

print("🚀 BOT FILE STARTED")

async def start(update, context):
    await update.message.reply_text("🤖 Bot is LIVE")

def main():
    try:
        print("📌 Building bot...")

        app = ApplicationBuilder().token(BOT_TOKEN).build()

        app.add_handler(CommandHandler("start", start))

        print("🤖 Starting polling (BOT SHOULD STAY ALIVE NOW)...")

        app.run_polling()

        print("❌ This should NEVER print (if it prints, bot exited)")

    except Exception as e:
        print("🔥 ERROR:")
        traceback.print_exc()

if __name__ == "__main__":
    main()