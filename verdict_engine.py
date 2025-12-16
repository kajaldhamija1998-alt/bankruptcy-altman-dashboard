import math

def final_verdict(z_score, o_score, ml_prob):
    # Convert Ohlson O-score to probability
    o_prob = 1 / (1 + math.exp(-o_score))

    flags = {
        "z_distress": z_score < 2.99,
        "o_distress": o_prob > 0.5,
        "ml_distress": ml_prob > 0.35
    }

    distress_count = sum(flags.values())

    if distress_count >= 1:
        return "Financial Distress Risk"
    else:
        return "Financially Stable"
