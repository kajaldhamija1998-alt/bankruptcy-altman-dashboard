import streamlit as st
from pdf_extractor import extract_financials
from altman import calculate_z_score

st.set_page_config(page_title="Bankruptcy Risk Dashboard")

st.title("📉 Bankruptcy Prediction Dashboard (Altman Z-Score)")

uploaded_file = st.file_uploader(
    "Upload Annual Report PDF", type="pdf"
)

market_value_equity = st.number_input(
    "Enter Market Value of Equity (₹)",
    min_value=0.0,
    step=1000000.0
)

if uploaded_file and market_value_equity > 0:
    with st.spinner("Reading annual report..."):
        data = extract_financials(uploaded_file)

    if None in data.values():
        st.error("Could not extract all required financial values from the PDF.")
    else:
        z_score = calculate_z_score(data, market_value_equity)

        st.subheader("Result")
        st.metric("Altman Z-Score", z_score)

        if z_score > 2.99:
            st.success("Safe Zone: Low Bankruptcy Risk")
        elif z_score >= 1.81:
            st.warning("Grey Zone: Moderate Financial Risk")
        else:
            st.error("Distress Zone: High Bankruptcy Risk")
