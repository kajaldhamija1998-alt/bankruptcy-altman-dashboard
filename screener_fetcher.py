import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_screener_data(company_code):
    url = f"https://www.screener.in/company/{company_code}/"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    tables = soup.find_all("table")
    data = {}

    for table in tables:
        for row in table.find_all("tr"):
            cols = [c.text.strip() for c in row.find_all(["th", "td"])]
            if len(cols) >= 2:
                data[cols[0].lower()] = cols[-1].replace(",", "")

    return data
