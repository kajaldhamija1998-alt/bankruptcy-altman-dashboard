def calculate_z_score(data, market_value_equity):
    X1 = data["working_capital"] / data["total_assets"]
    X2 = data["retained_earnings"] / data["total_assets"]
    X3 = data["ebit"] / data["total_assets"]
    X4 = market_value_equity / data["total_liabilities"]
    X5 = data["sales"] / data["total_assets"]

    z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5
    return round(z, 2)
