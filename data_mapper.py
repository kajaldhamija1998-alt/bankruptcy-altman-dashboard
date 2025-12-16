def map_financials(raw):
    def safe(key, default=1):
        val = raw.get(key)
        if val in [None, 0]:
            return default
        return val

    total_assets = safe("total_assets")
    total_liabilities = safe("total_liabilities")
    sales = safe("sales")
    ebit = safe("ebit")
    market_value_equity = safe("market_value_equity")

    # Conservative academic proxies
    current_assets = 0.4 * total_assets      # standard proxy
    current_liabilities = 0.3 * total_liabilities
    net_income = 0.7 * ebit                   # accounting proxy
    retained_earnings = 0.5 * total_assets
    cfo = 0.8 * ebit

    return {
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,
        "current_assets": current_assets,
        "current_liabilities": current_liabilities,
        "sales": sales,
        "net_income": net_income,
        "retained_earnings": retained_earnings,
        "ebit": ebit,
        "market_value_equity": market_value_equity,
        "cfo": cfo
    }
