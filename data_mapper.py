def map_financials(raw):
    def safe(key, default=0):
        return raw.get(key) if raw.get(key) not in [None] else default

    return {
        "total_assets": safe("total_assets", 1),
        "total_liabilities": safe("total_liabilities", 1),
        "current_assets": safe("current_assets", 1),
        "current_liabilities": safe("current_liabilities", 1),
        "sales": safe("sales", 1),
        "net_income": safe("net_income", 1),
        "retained_earnings": safe("retained_earnings", 0),
        "ebit": safe("ebit", 0),
        "market_value_equity": safe("market_value_equity", 1),
        "cfo": safe("cfo", 0),
    }
