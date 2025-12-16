import requests
from bs4 import BeautifulSoup

def fetch_screener_data(company_code):
    url = f"https://www.screener.in/company/{company_code}/consolidated/"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    data = {}

    # find all list entries with name + number
    rows = soup.select("li.flex.flex-space-between")

    for row in rows:
        # label is the left text
        label_tag = row.select_one(".name")
        value_tag = row.select_one(".number")

        if not label_tag or not value_tag:
            continue

        key = label_tag.text.strip().lower()
        val_str = (
            value_tag.text
            .replace(",", "")
            .replace("₹", "")
            .replace("Cr", "")
            .replace("(", "-")
            .replace(")", "")
            .strip()
        )

        try:
            val = float(val_str)
        except:
            continue

        # map known text to our keys
        if "sales" in key:
            data["sales"] = val
        if "total assets" in key:
            data["total_assets"] = val
        if "total liabilities" in key:
            data["total_liabilities"] = val
        if "operating profit" in key:
            data["ebit"] = val
        if "net profit" in key:
            data["net_income"] = val
        if "market cap" in key:
            data["market_value_equity"] = val
        if "cash from operations" in key:
            data["cfo"] = val
        if "current assets" in key:
            data["current_assets"] = val
        if "current liabilities" in key:
            data["current_liabilities"] = val
        if "reserves" in key:
            data["retained_earnings"] = val

    return data
