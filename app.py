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
   firm_type = fin["company_type"]

z_score = calculate_z_score(fin, firm_type)

    )

    # -------- Ohlson O-Score --------
    o_score, p_bankruptcy = calculate_o_score(fin)

    # -------- Stress Indicators --------
    stress = stress_indicators(fin)

    # -------- Final Verdict (NO REGRESSION) --------
    verdict = final_verdict(z_score, o_score, stress, firm_type, p_bankruptcy)

    )

    st.subheader("Results")
    st.metric("Altman Z-Score", round(z_score, 2))
    st.metric("Probability of Bankruptcy", round(p_bankruptcy, 3))

    st.subheader("Stress Indicators")
    st.json(stress)

    st.subheader("Final Assessment")
    st.success(verdict)
