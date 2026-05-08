import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

CHANNEL_IDS = list(map(int, os.getenv("CHANNEL_IDS").split(",")))

# Session Timings
MORNING_SESSION_TIME = "10:00"
EVENING_SESSION_TIME = "20:00"

# Daily Prediction Limits
PREDICTIONS_PER_SESSION = 10
TOTAL_DAILY_PREDICTIONS = 20

# Win Rate Logic
MIN_WINS = 8
MAX_WINS = 10

# AI Confidence Range
MIN_CONFIDENCE = 90
MAX_CONFIDENCE = 99

# Prediction Types
COLORS = ["GREEN 🟢", "RED 🔴"]
PREDICTIONS = ["BIG", "SMALL"]

# Asset Paths
WIN_GIF = "assets/images/win.gif"
LOSS_GIF = "assets/images/loss.gif"

GOOD_MORNING_IMAGE = "assets/images/good_morning.jpg"
GOOD_NIGHT_IMAGE = "assets/images/good_night.jpg"

# Database
DATABASE_NAME = "vip_prediction_bot.db"