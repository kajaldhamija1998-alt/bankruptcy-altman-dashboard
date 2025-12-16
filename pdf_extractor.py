import pdfplumber
import re

def extract_financials(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    def find_number(pattern):
        match = re.search(pattern, text, re.IGNORECASE)
        return float(match.group(1).replace(",", "")) if match else None

    return {
        "total_assets": find_number(r"Total Assets\s*([\d,]+)"),
        "total_liabilities": find_number(r"Total Liabilities\s*([\d,]+)"),
        "working_capital": find_number(r"Working Capital\s*([\d,]+)"),
        "retained_earnings": find_number(r"Retained Earnings\s*([\d,]+)"),
        "ebit": find_number(r"EBIT\s*([\d,]+)"),
        "sales": find_number(r"Revenue\s*([\d,]+)")
    }
