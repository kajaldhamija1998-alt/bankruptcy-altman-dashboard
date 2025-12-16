import streamlit as st

from screener_fetcher import fetch_screener_data
from data_mapper import map_financials
from altman import calculate_z_score
from ohlson import calculate_o_score
from stress_checks import stress_indicators
from verdict_engine import final_verdict

import joblib
import pandas as pd

st.set_page_config(page_title="Automated Financial Distress Predictor")

st.title("📉 Automated Bankruptcy & Financial Distress Prediction")

company_code = st.text_input(
    "Enter Company Code (as per Screener.in)",
    value="TATAMOTORS"
)

if st.button("Analyze Company"):

    with st.spinner("Fetching financial data from Screener..."):
        raw_data = fetch_screener_data(company_code)

    if not raw_data:
        st.error("Could not fetch data. Check company code.")
        st.stop()

    financials = map_financials(raw_data)

    st.subheader("Extracted Financial Data")
    st.dataframe(pd.DataFrame(financials.items(), columns=["Metric", "Value"]))

    # -------- Altman Z-score --------
    z_score = calculate_z_score(
        {
            "working_capital": financials["current_assets"] - financials["current_liabilities"],
            "retained_earnings": financials["retained_earnings"],
            "ebit": financials["ebit"],
            "total_assets": financials["total_assets"],
            "total_liabilities": financials["total_liabilities"],
            "sales": financials["sales"]
        },
        market_value_equity=financials["total_assets"]  # proxy
    )

    # -------- Ohlson O-score --------
    o_score = calculate_o_score(financials)


    # -------- Stress Indicators --------
    stress = stress_indicators(financials)

    # -------- Logistic Regression --------
    model = joblib.load("regression_model.pkl")

    X = [[
        (financials["current_assets"] - financials["current_liabilities"]) / financials["total_assets"],
        financials["retained_earnings"] / financials["total_assets"],
        financials["ebit"] / financials["total_assets"],
        financials["total_liabilities"] / financials["total_assets"],
        financials["cfo"] / max(financials["total_liabilities"], 1)
    ]]

    prob = model.predict_proba(X)[0][1]

    # -------- Final Verdict --------
    verdict = final_verdict(z_score, o_score, stress, prob)

    st.subheader("Results")
    st.metric("Altman Z-Score", round(z_score, 2))
    st.metric("Ohlson O-Score", round(o_score, 2))
    st.metric("Probability of Distress", round(prob, 2))

    st.subheader("Final Assessment")
    st.success(verdict)
