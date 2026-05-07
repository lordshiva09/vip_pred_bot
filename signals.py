import random
from config import COLORS, PREDICTIONS

# Global Round Number
round_number = 745

# =========================
# GENERATE SIGNAL
# =========================

def generate_signal():

    global round_number

    color = random.choice(COLORS)
    prediction = random.choice(PREDICTIONS)

    accuracy = random.randint(90, 99)

    confidence_levels = [
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY HIGH"
    ]

    confidence = random.choice(confidence_levels)

    message = f"""
╔══════════════════╗
   🔥 VIP SIGNAL 🔥
╚══════════════════╝

🎯 ROUND : {round_number}

🟢 COLOR : {color}
📊 PREDICTION : {prediction}

📈 ACCURACY : {accuracy}%
🧠 AI CONFIDENCE : {confidence}

━━━━━━━━━━━━━━
⚡ PLAY SAFE
💎 PREMIUM ENTRY
━━━━━━━━━━━━━━

⏰ NEXT ROUND : {round_number + 1}
🚀 STAY CONNECTED
"""

    round_number += 1

    return message