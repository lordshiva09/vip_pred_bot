from scheduler import scheduler, start_scheduler
import asyncio

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)

from config import BOT_TOKEN, ADMIN_ID
from signals import generate_signal
from ai_engine import generate_session_results

# =========================
# SESSION DATA
# =========================

session_results, session_mode = generate_session_results()

current_result_index = 0

# =========================
# START COMMAND
# =========================

async def start_command(update, context):

    user_id = update.effective_user.id

    if user_id != ADMIN_ID:
        await update.message.reply_text(
            "❌ Unauthorized User"
        )
        return

    await update.message.reply_text(
        f"🔥 VIP Prediction Bot Running 🔥\n\nMODE : {session_mode}"
    )

# =========================
# SIGNAL COMMAND
# =========================

async def signal_command(update, context):

    global current_result_index

    user_id = update.effective_user.id

    if user_id != ADMIN_ID:
        await update.message.reply_text(
            "❌ Unauthorized User"
        )
        return

    # Send Prediction
    signal_message = generate_signal()

    await update.message.reply_text(signal_message)

    # Wait 1 Minute
    await asyncio.sleep(60)

    # Result Logic
    result = session_results[current_result_index]

    if result == "WIN":

        result_message = f"""
🏆 RESULT : WIN ✅

🔥 CONGRATULATIONS
💎 VIP SIGNAL SUCCESSFUL
"""

    else:

        result_message = f"""
❌ RESULT : LOSS

♻️ RECOVERY SIGNAL SOON
⚡ STAY READY
"""

    await update.message.reply_text(result_message)

    current_result_index += 1

    # Reset After 10 Predictions
    if current_result_index >= 10:

        current_result_index = 0

# =========================
# MAIN FUNCTION
# =========================
# =========================
# AUTO SESSION
# =========================

async def auto_session(bot):

    global current_result_index

    for i in range(10):

        # SEND SIGNAL
        signal_message = generate_signal()

        await bot.send_message(
            chat_id="-1003978872708",
            text=signal_message
        )

        # WAIT 1 MINUTE
        await asyncio.sleep(60)

        # RESULT
        result = session_results[current_result_index]

        if result == "WIN":

            result_message = """
🏆 RESULT : WIN ✅

🔥 CONGRATULATIONS
💎 VIP SIGNAL SUCCESSFUL
"""

        else:

            result_message = """
❌ RESULT : LOSS

♻️ RECOVERY SIGNAL SOON
"""

        # SEND RESULT
        await bot.send_message(
            chat_id="-1003978872708",
            text=result_message
        )

        current_result_index += 1

        # SMALL DELAY
        await asyncio.sleep(10)

def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("signal", signal_command))

    print("🚀 VIP Prediction Bot Running...")

    # START SCHEDULER
    start_scheduler()

    # MORNING SESSION
    scheduler.add_job(
        lambda: asyncio.create_task(
            auto_session(app.bot)
        ),
        trigger="cron",
        hour=10,
        minute=0
    )

    # EVENING SESSION
    scheduler.add_job(
        lambda: asyncio.create_task(
            auto_session(app.bot)
        ),
        trigger="cron",
        hour=20,
        minute=0
    )

    # RUN BOT
    app.run_polling()

# =========================
# RUN BOT
# =========================

if __name__ == "__main__":
    main()