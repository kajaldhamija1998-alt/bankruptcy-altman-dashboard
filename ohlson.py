def calculate_o_score(fin):
    # Safely extract values
    total_assets = fin.get("total_assets", 0) or 0
    total_liabilities = fin.get("total_liabilities", 0) or 0
    current_assets = fin.get("current_assets", 0) or 0
    current_liabilities = fin.get("current_liabilities", 0) or 0
    net_income = fin.get("net_income", 0) or 0
    prev_net_income = fin.get("prev_net_income", net_income) or net_income

    # Prevent division by zero
    total_assets = max(total_assets, 1)
    current_assets = max(current_assets, 1)

    o_score = (
        -1.32
        - 0.407 * (net_income / total_assets)
        + 6.03 * (total_liabilities / total_assets)
        + 0.076 * (current_liabilities / current_assets)
        - 1.43 * (1 if net_income > 0 else 0)
        - 2.37 * (1 if net_income > prev_net_income else 0)
    )

    return o_score
