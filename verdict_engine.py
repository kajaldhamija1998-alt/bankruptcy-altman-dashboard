def final_verdict(z_score, o_score, stress, prob=None):
    """
    Finance-theory based verdict (NO ML dependency)
    """

    red_flags = sum(stress.values())

    if z_score < 1.81 or o_score > 0.5 or red_flags >= 2:
        return "⚠️ High Risk of Financial Distress"

    if 1.81 <= z_score <= 2.99:
        return "⚠️ Grey Zone – Monitor Closely"

    return "✅ Financially Stable"
