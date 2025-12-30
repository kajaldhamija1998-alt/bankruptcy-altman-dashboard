import streamlit as st
import pandas as pd

from altman import calculate_z_score
from ohlson import calculate_o_score
from stress_checks import stress_indicators
from verdict_engine import final_verdict

st.set_page_config(page_title="AI Bankruptcy Predictor")

st.title("📉 AI-Based Bankruptcy & Financial Distress Predictor")

st.markdown("""
Upload a CSV containing annual financials.
Required columns:

company_type,
current_assets, current_liabilities,
total_assets, total_liabilities,
retained_earnings, ebit, sales,
market_value_equity, net_income, cfo
""")

uploaded = st.file_uploader("Upload Financials CSV", type="csv")

if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.dataframe(df)

    fin = df.iloc[-1].to_dict()

    firm_type = fin["company_type"]

    z_score = calculate_z_score(fin, firm_type)
    o_score = calculate_o_score(fin)
    stress = stress_indicators(fin)

    verdict = final_verdict(z_score, o_score, stress, None)

    st.subheader("Results")
    st.metric("Altman Z-Score", round(z_score, 2))
    st.metric("Ohlson O-Score", round(o_score, 2))

    st.subheader("Stress Indicators")
    st.json(stress)

    st.subheader("Final Verdict")
    st.success(verdict)
