import requests
from bs4 import BeautifulSoup

def clean_number(x):
    try:
        return float(
            x.replace(",", "")
             .replace("₹", "")
             .replace("%", "")
             .strip()
        )
    except:
        return None


def fetch_screener_data(company_code):
    url = f"https://www.screener.in/company/{company_code}/"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    tables = soup.find_all("table")
    data = {}

    for table in tables:
        for row in table.find_all("tr"):
            cols = [c.text.]()
