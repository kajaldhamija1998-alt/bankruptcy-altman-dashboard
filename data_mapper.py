def map_financials(raw):
    def get(*keys):
        for k in keys:
            if k in raw and raw[k] is not None:
                return raw[k]
        return 0

    return {
        "total_assets": get("total assets", "total assets (₹ cr)", "assets"),
        "total_liabilities": get(
            "total liabilities",
            "total liabilities (₹ cr)",
            "liabilities"
        ),
        "current_assets": get(
            "current assets",
            "current assets (₹ cr)"
        ),
        "current_liabilities": get(
            "current liabilities",
            "current liabilities (₹ cr)"
        ),
        "net_income": get(
            "net profit",
            "profit after tax",
            "net income"
        ),
        "retained_earnings": get(
            "reserves",
            "retained earnings"
        ),
        "ebit": get(
            "operating profit",
            "ebit"
        ),
        "market_value_equity": get(
            "market cap",
            "market capitalization"
        ),
        "sales": get(
            "sales",
            "revenue"
        )
    }
