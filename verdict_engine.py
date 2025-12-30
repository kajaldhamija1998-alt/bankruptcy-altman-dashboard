def final_verdict(z_score, o_score, stress, firm_type, p_bankruptcy):

    # Ohlson override – if default probability is high
    if o_score > 0.5:
        return "🚨 Very High Bankruptcy Risk (Ohlson Default Zone)"

    if firm_type == "public_manufacturing":
        if z_score > 2.99:
            return "✅ Financially Stable"
        if z_score >= 1.8:
            return "⚠️ Grey Zone – Monitor Closely"
        return "⚠️ High Risk of Financial Distress"

    if firm_type == "private_manufacturing":
        if z_score > 2.9:
            return "✅ Financially Stable"
        return "⚠️ High Risk of Financial Distress"

    if firm_type == "non_manufacturing":
        if z_score > 2.6:
            return "✅ Financially Stable"
        return "⚠️ High Risk of Financial Distress"

    return "Classification Error"
