import random

def generate_session_results():

    results = []

    # 10 RESULT GENERATE
    for i in range(10):

        # 80% WIN
        result = random.choices(
            ["WIN", "LOSS"],
            weights=[80, 20],
            k=1
        )[0]

        results.append(result)

    # RANDOM MODE
    modes = [
        "SAFE MODE",
        "AI MODE",
        "VIP MODE",
        "PREMIUM MODE"
    ]

    session_mode = random.choice(modes)

    return results, session_mode