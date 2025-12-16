def calculate_z_score(fin, market_value_equity):
    """
    Altman Z-Score (Manufacturing, public firms)
    Z = 1.2X1 + 1.4X2 + 3.3X3 + 0.6X4 + 1.0X5
    """

    ta = fin["total_assets"]
    if ta == 0:
        return 0

    X1 = fin["working_capital"] / ta
    X2 = fin["retained_earnings"] / ta
    X3 = fin["ebit"] / ta
    X4 = market_value_equity / fin["total_liabilities"] if fin["total_liabilities"] > 0 else 0
    X5 = fin["sales"] / ta

    z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5
    return z
