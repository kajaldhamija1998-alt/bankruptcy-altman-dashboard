def map_financials(raw):
    def get(*keys):
        for k in keys:
            if k in raw and raw[k] not in [None, 0]:
                return raw[k]
        return 0

    # Working Capital proxy
    working_capital = get("working capital")

    total_assets = get("total assets")
    total_liabilities = get("total liabilities")

    return {
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,

        # Approximation (standard practice)
        "current_assets": max(working_capital, 0),
        "current_liabilities": max(-working_capital, 0),

        "sales": get("sales"),
        "net_income": get("net profit"),
        "retained_earnings": get("reserves"),
        "ebit": get("operating profit"),
        "market_value_equity": get("market cap"),

        # CFO proxy
        "cfo": get("operating profit")
    }
