def stress_indicators(fin):
    stress = {}

    stress["negative_cfo"] = fin["cfo"] < 0
    stress["interest_cover"] = fin["ebit"] / max(fin["interest"], 1)

    stress["debt_ratio"] = fin["total_liabilities"] / fin["total_assets"]

    return stress
