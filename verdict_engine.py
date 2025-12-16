def final_verdict(z_score, o_score, stress, prob):
    """
    z_score : Altman Z-score
    o_score : Ohlson O-score
    stress  : dict from stress_checks
    prob    : logistic regression probability
    """

    if (z_score < 1.81 or o_score > 0) and prob > 0.5:
        return "High Financial Distress / Bankruptcy Risk"

    if stress["negative_cfo"] or stress["interest_cover"] < 1.5:
        return "Moderate Financial Stress"

    return "Financially Stable"
