import random
import asyncio

from scheduler import scheduler, start_scheduler

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN, ADMIN_ID, CHANNEL_IDS
from ai_engine import generate_session_results

# =========================
# SESSION DATA
# =========================

session_results, session_mode = generate_session_results()
current_result_index = 0

# RANDOM START NUMBER
base_number = random.randint(100, 999)

# STICKER / GIF FILE IDs
WIN_GIF = "CAACAgUAAxkBAAM-af1iPRalLhzOokUcDwHL7eVZVt4AAp4OAALReAABVN7oQLXNcEHWOwQ"
LOSS_GIF = "CAACAgUAAxkBAANIaf1puYucpjH2rEYcr8B4uMPoKgcAAh4aAALAgFhXTSI0JHjaipc7BA"

# =========================
# SIGNAL GENERATOR
# =========================

def generate_signal():
    global base_number

    confidence_levels = ["LOW", "MEDIUM", "HIGH"]

    combinations = [
        ("RED 🔴", "SMALL"),
        ("RED 🔴", "BIG"),
        ("GREEN 🟢", "SMALL"),
        ("GREEN 🟢", "BIG"),
    ]

    selected_color, selected_prediction = random.choice(combinations)

    signal = f"""
╔══════════════════╗
   🔥 VIP SIGNAL 🔥
╚══════════════════╝

🎯 ROUND : {base_number}

🟢 COLOR : {selected_color}
📊 PREDICTION : {selected_prediction}

📈 ACCURACY : {random.randint(91, 99)}%
🧠 AI CONFIDENCE : {random.choice(confidence_levels)}

━━━━━━━━━━━━━━
⚡️ PLAY SAFE
💎 PREMIUM ENTRY
━━━━━━━━━━━━━━

⏰ NEXT ROUND : {base_number + 1}
🚀 STAY CONNECTED
"""

    base_number += 1

    if base_number > 999:
        base_number = random.randint(100, 999)

    return signal


# =========================
# START COMMAND
# =========================

async def start_command(update, context):
    user_id = update.effective_user.id

    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ Unauthorized User")
        return

    await update.message.reply_text(
        f"🔥 VIP Prediction Bot Running 🔥\n\nMODE : {session_mode}"
    )


# =========================
# GET FILE ID
# =========================

async def get_file_id(update, context):

    if update.message.sticker:
        await update.message.reply_text(
            f"STICKER FILE ID:\n\n{update.message.sticker.file_id}"
        )

    elif update.message.animation:
        await update.message.reply_text(
            f"GIF FILE ID:\n\n{update.message.animation.file_id}"
        )

    else:
        await update.message.reply_text("❌ Sticker ya GIF bhejo")


# =========================
# SIGNAL COMMAND (FIXED)
# =========================

async def signal_command(update, context):

    global current_result_index

    user_id = update.effective_user.id

    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ Unauthorized User")
        return

    signal_message = generate_signal()

    # SEND SIGNAL TO ALL CHANNELS
    for channel in CHANNEL_IDS:
        await context.bot.send_message(
            chat_id=channel,
            text=signal_message
        )

    await asyncio.sleep(30)

    result = session_results[current_result_index]

    if result == "WIN":

        for channel in CHANNEL_IDS:

            await context.bot.send_sticker(
                chat_id=channel,
                sticker=WIN_GIF
            )

            await context.bot.send_message(
                chat_id=channel,
                text="🏆 RESULT : WIN ✅\n\n🔥 CONGRATULATIONS 💎 VIP SIGNAL SUCCESSFUL"
            )

    else:

        for channel in CHANNEL_IDS:

            await context.bot.send_sticker(
                chat_id=channel,
                sticker=LOSS_GIF
            )

            await context.bot.send_message(
                chat_id=channel,
                text="❌ RESULT : LOSS\n\n♻️ RECOVERY SIGNAL SOON"
            )

    current_result_index += 1

    if current_result_index >= len(session_results):
        current_result_index = 0


# =========================
# AUTO SESSION (FIXED)
# =========================

async def auto_session(bot):

    global current_result_index

    for _ in range(10):

        signal_message = generate_signal()

        for channel in CHANNEL_IDS:
            await bot.send_message(
                chat_id=channel,
                text=signal_message
            )

        await asyncio.sleep(30)

        result = session_results[current_result_index]

        if result == "WIN":

            for channel in CHANNEL_IDS:

                await bot.send_sticker(
                    chat_id=channel,
                    sticker=WIN_GIF
                )

                await bot.send_message(
                    chat_id=channel,
                    text="🏆 RESULT : WIN ✅\n\n🔥 CONGRATULATIONS 💎 VIP SIGNAL SUCCESSFUL"
                )

        else:

            for channel in CHANNEL_IDS:

                await bot.send_sticker(
                    chat_id=channel,
                    sticker=LOSS_GIF
                )

                await bot.send_message(
                    chat_id=channel,
                    text="❌ RESULT : LOSS\n\n♻️ RECOVERY SIGNAL SOON"
                )

        current_result_index += 1

        if current_result_index >= len(session_results):
            current_result_index = 0

        await asyncio.sleep(10)


# =========================
# MAIN
# =========================

def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("signal", signal_command))

    app.add_handler(
        MessageHandler(
            filters.Sticker.ALL | filters.ANIMATION,
            get_file_id
        )
    )

    print("🚀 VIP Prediction Bot Running...")

    start_scheduler()

    scheduler.add_job(
        lambda: asyncio.create_task(auto_session(app.bot)),
        trigger="cron",
        hour=10,
        minute=0
    )

    scheduler.add_job(
        lambda: asyncio.create_task(auto_session(app.bot)),
        trigger="cron",
        hour=20,
        minute=0
    )

    app.run_polling()


# =========================
# RUN
# =========================

import traceback

if __name__ == "__main__":
    try:
        print("🚀 BOT STARTING...")
        main()
    except Exception as e:
        print("❌ ERROR OCCURRED:")
        print(traceback.format_exc())