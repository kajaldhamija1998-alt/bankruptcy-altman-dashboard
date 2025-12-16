import streamlit as st
from pdf_extractor import extract_financials
from altman import calculate_z_score
from ohlson import calculate_o_score

st.set_page_config(page_title="Bankruptcy Risk Dashboard")

st.title("📉 Bankruptcy Prediction Dashboard (Altman Z-Score)")

st.write("Upload annual report PDF or enter values manually if extraction fails.")

uploaded_file = st.file_uploader("Upload Annual Report (PDF)", type="pdf")

st.subheader("Market Data")
market_value_equity = st.number_input(
    "Market Value of Equity (Market Capitalization)",
    min_value=0.0
)

data = None

if uploaded_file:
    with st.spinner("Extracting financial data from PDF..."):
        data = extract_financials(uploaded_file)

    if data is None or None in data.values():
        st.warning("PDF extraction incomplete. Please enter values manually.")

st.subheader("Financial Inputs")

working_capital = st.number_input(
    "Working Capital",
    value=0.0 if not data else data["working_capital"] or 0.0
)
retained_earnings = st.number_input(
    "Retained Earnings",
    value=0.0 if not data else data["retained_earnings"] or 0.0
)
ebit = st.number_input(
    "EBIT",
    value=0.0 if not data else data["ebit"] or 0.0
)
total_assets = st.number_input(
    "Total Assets",
    value=1.0 if not data else data["total_assets"] or 1.0
)
total_liabilities = st.number_input(
    "Total Liabilities",
    value=1.0 if not data else data["total_liabilities"] or 1.0
)
sales = st.number_input(
    "Sales / Revenue",
    value=1.0 if not data else data["sales"] or 1.0
)

if st.button("Calculate Z-Score"):
    inputs = {
        "working_capital": working_capital,
        "retained_earnings": retained_earnings,
        "ebit": ebit,
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,
        "sales": sales
    }

    z = calculate_z_score(inputs, market_value_equity)

    st.metric("Altman Z-Score", z)

    if z > 2.99:
        st.success("Safe Zone: Low Bankruptcy Risk")
    elif z >= 1.81:
        st.warning("Grey Zone: Moderate Risk")
    else:
        st.error("Distress Zone: High Bankruptcy Risk")
        
st.divider()
st.header("📊 Ohlson O-Score (Bankruptcy Probability Model)")

current_assets = st.number_input("Current Assets", value=1.0)
current_liabilities = st.number_input("Current Liabilities", value=1.0)
net_income = st.number_input("Net Income (Current Year)", value=0.0)
prev_net_income = st.number_input("Net Income (Previous Year)", value=0.0)

if st.button("Calculate O-Score"):
    o_score = calculate_o_score(
        total_assets,
        total_liabilities,
        working_capital,
        current_assets,
        current_liabilities,
        net_income,
        prev_net_income
    )

    st.metric("Ohlson O-Score", o_score)

    if o_score > 0:
        st.error("High probability of bankruptcy")
    else:
        st.success("Low probability of bankruptcy")
