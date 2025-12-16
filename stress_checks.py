def stress_indicators(fin):
    stress = {}

    cfo = fin.get("cfo", 0) or 0
    ebit = fin.get("ebit", 0) or 0
    interest = fin.get("interest", 0) or 0
    total_liabilities = fin.get("total_liabilities", 0) or 0
    total_assets = fin.get("total_assets", 0) or 1

    stress["negative_cfo"] = cfo < 0

    # Interest coverage
    stress["interest_cover"] = (
        ebit / interest if interest > 0 else float("inf")
    )

    # Debt ratio
    stress["debt_ratio"] = total_liabilities / max(total_assets, 1)

    return stress
