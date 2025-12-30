def calculate_z_score(fin, firm_type):
    ca = fin["current_assets"]
    cl = fin["current_liabilities"]
    ta = fin["total_assets"]
    tl = fin["total_liabilities"]

    wc = ca - cl

    X1 = wc / ta
    X2 = fin["retained_earnings"] / ta
    X3 = fin["ebit"] / ta
    X4 = fin["market_value_equity"] / tl
    X5 = fin["sales"] / ta

    # Manufacturing Public
    if firm_type == "public_manufacturing":
        z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5

    # Manufacturing Private
    elif firm_type == "private_manufacturing":
        z = 0.717*X1 + 0.847*X2 + 3.107*X3 + 0.420*X4 + 0.998*X5

    # Non-Manufacturing
    else:
        z = 6.56*X1 + 3.26*X2 + 6.72*X3 + 1.05*X4

    return z
