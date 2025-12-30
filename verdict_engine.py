def final_verdict(z_score, o_score, stress, firm_type, p_bankruptcy):

    # Bankruptcy override
    if o_score > 0.5:
        return "🚨 Very High Bankruptcy Risk (Ohlson Default Zone)"

    # PUBLIC MANUFACTURING
    if firm_type == "public_manufacturing":
        if z_score > 2.99:
            return "✅ Financially Stable"
        elif z_score >= 1.8:
            return "⚠️ Grey Zone – Monitor Closely"
        else:
            return "⚠️ High Risk of Financial Distress"

    # PRIVATE MANUFACTURING
    elif firm_type == "private_manufacturing":
        if z_score > 2.9:
            return "✅ Financially Stable"
        elif z_score >= 1.23:
            return "⚠️ Grey Zone – Monitor Closely"
        else:
            return "⚠️ High Risk of Financial Distress"

    # NON MANUFACTURING
    else:
        if z_score > 2.6:
            return "✅ Financially Stable"
        elif z_score >= 1.1:
            return "⚠️ Grey Zone – Monitor Closely"
        else:
            return "⚠️ High Risk of Financial Distress"
