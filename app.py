import streamlit as st
import pandas as pd
from altman import calculate_z_score
from ohlson import calculate_o_score
from stress_checks import stress_indicators
from verdict_engine import final_verdict

st.set_page_config(page_title="AI Bankruptcy Predictor")
st.title("AI Bankruptcy & Financial Distress Predictor")

uploaded = st.file_uploader("Upload Financial CSV", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    fin = df.iloc[-1].to_dict()

    firm_type = fin["company_type"]

    z = calculate_z_score(fin, firm_type)
    o = calculate_o_score(fin)
    stress = stress_indicators(fin)

    verdict = final_verdict(z, o, stress, None)

    st.metric("Altman Z-Score", round(z,2))
    st.metric("Ohlson O-Score", round(o,2))
    st.json(stress)
    st.success(verdict)
