import streamlit as st
import pandas as pd

from altman import calculate_z_score
from ohlson import calculate_o_score
from stress_checks import stress_indicators
from verdict_engine import final_verdict

st.set_page_config(page_title="Automated Financial Distress Predictor")

st.title("📉 Automated Bankruptcy & Financial Distress Prediction")

st.markdown("""
### Instructions
Upload a **CSV file** containing financial statement data.
The model will automatically compute:
- Altman Z-Score
- Ohlson O-Score
- Financial Stress Indicators
- Final Distress Verdict
""")

uploaded = st.file_uploader("Upload Financials CSV", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)

    st.subheader("Uploaded Financial Data")
    st.dataframe(df)

    # Use latest year
    fin = df.iloc[-1].to_dict()

    # -------- Altman Z-Score --------
    z_score = calculate_z_score(
        {
            "working_capital": fin["current_assets"] - fin["current_liabilities"],
            "retained_earnings": fin["retained_earnings"],
            "ebit": fin["ebit"],
            "total_assets": fin["total_assets"],
            "total_liabilities": fin["total_liabilities"],
            "sales": fin["sales"]
        },
        market_value_equity=fin["market_value_equity"]
    )

    # -------- Ohlson O-Score --------
    o_score = calculate_o_score(fin)

    # -------- Stress Indicators --------
    stress = stress_indicators(fin)

    # -------- Final Verdict (NO REGRESSION) --------
    verdict = final_verdict(
        z_score=z_score,
        o_score=o_score,
        stress=stress,
        prob=None
    )

    st.subheader("Results")
    st.metric("Altman Z-Score", round(z_score, 2))
    st.metric("Ohlson O-Score", round(o_score, 2))

    st.subheader("Stress Indicators")
    st.json(stress)

    st.subheader("Final Assessment")
    st.success(verdict)
