print("FILE STARTED")

try:
    print("IMPORTING CONFIG")
    from config import BOT_TOKEN, ADMIN_ID

    print("IMPORTING TELEGRAM")
    from telegram.ext import ApplicationBuilder

    print("IMPORT SUCCESS")

except Exception as e:
    print("🔥 IMPORT ERROR:")
    import traceback
    traceback.print_exc()

print("END FILE")