import random

# =========================
# SESSION RESULT LOGIC
# =========================

def generate_session_results():

    modes = [
        ("NORMAL", 8),
        ("VIP", 9),
        ("JACKPOT", 10)
    ]

    selected_mode = random.choice(modes)

    mode_name = selected_mode[0]
    total_wins = selected_mode[1]

    results = ["WIN"] * total_wins
    results += ["LOSS"] * (10 - total_wins)

    random.shuffle(results)

    # Prevent too many continuous losses
    for i in range(len(results) - 1):

        if results[i] == "LOSS" and results[i + 1] == "LOSS":

            results[i + 1] = "WIN"

    return results, mode_name