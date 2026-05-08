import random

def generate_signal():

    start_number = random.randint(100, 997)

    signal = f"""
🔥 VIP PREDICTION 🔥

🎯 ENTRY :
{start_number}

🎯 TARGET :
{start_number + 1}

🎯 SAFE :
{start_number + 2}
"""

    return signal