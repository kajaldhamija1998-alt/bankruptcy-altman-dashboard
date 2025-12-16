def stress_indicators(fin):
    stress = {}

    stress["negative_net_income"] = fin["net_income"] < 0
    stress["negative_cfo"] = fin["cfo"] < 0
    stress["high_leverage"] = (
        fin["total_liabilities"] / fin["total_assets"] > 0.6
        if fin["total_assets"] > 0 else False
    )
    stress["low_liquidity"] = (
        fin["current_assets"] / fin["current_liabilities"] < 1
        if fin["current_liabilities"] > 0 else False
    )

    return stress
