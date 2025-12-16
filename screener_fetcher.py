import requests
from bs4 import BeautifulSoup

def fetch_screener_data(company_code):
    url = f"https://www.screener.in/company/{company_code}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    data = {
        "sales": None,
        "total_assets": None,
        "total_liabilities": None,
        "ebit": None,
        "market_value_equity": None,
        "current_assets": None,
        "current_liabilities": None,
        "net_income": None,
        "retained_earnings": None,
        "cfo": None
    }

    # ---- Extract key-value pairs ----
    for row in soup.select("li.flex.flex-space-between"):
        label = row.select_one(".name")
        value = row.select_one(".number")

        if not label or not value:
            continue

        key = label.text.strip().lower()
        val = value.text.replace(",", "").replace("₹", "").strip()

        try:
            val = float(val)
        except:
            continue

        if "sales" in key:
            data["sales"] = val
        elif "total assets" in key:
            data["total_assets"] = val
        elif "total liabilities" in key:
            data["total_liabilities"] = val
        elif "operating profit" in key:
            data["ebit"] = val
        elif "market cap" in key:
            data["market_value_equity"] = val

    return data
