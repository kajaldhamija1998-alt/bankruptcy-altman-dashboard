def map_financials(raw):
    return {
        "total_assets": float(raw.get("total assets", 0)),
        "total_liabilities": float(raw.get("total liabilities", 0)),
        "current_assets": float(raw.get("current assets", 0)),
        "current_liabilities": float(raw.get("current liabilities", 0)),
        "retained_earnings": float(raw.get("reserves & surplus", 0)),
        "sales": float(raw.get("sales", 0)),
        "ebit": float(raw.get("operating profit", 0)),
        "interest": float(raw.get("interest", 0)),
        "net_income": float(raw.get("net profit", 0)),
        "cfo": float(raw.get("cash from operating activity", 0))
    }
