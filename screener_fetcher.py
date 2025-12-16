import requests
from bs4 import BeautifulSoup


def clean_number(text):
    try:
        return float(
            text.replace(",", "")
                .replace("₹", "")
                .replace("%", "")
                .strip()
        )
    except:
        return None


def fetch_screener_data(company_code):
    url = f"https://www.screener.in/company/{company_code}/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    data = {}

    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            cols = [c.text.strip() for c in row.find_all(["th", "td"])]

            if len(cols) < 2:
                continue

            key = cols[0].lower()

            for val in reversed(cols[1:]):
                num = clean_number(val)
                if num is not None:
                    data[key] = num
                    break

    return data
