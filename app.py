# =============================
# Supply Chain Emissions App
# =============================

import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

from utils.preprocessor import preprocess_input

# -----------------------------
# Safe Path Handling
# -----------------------------
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, 'models', 'LR_model.pkl')
scaler_path = os.path.join(BASE_DIR, 'models', 'scaler.pkl')

# -----------------------------
# Load Model and Scaler
# -----------------------------
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# -----------------------------
# App Title & Instructions
# -----------------------------
st.title("Supply Chain Emissions Prediction")

st.markdown("""
This app predicts **Supply Chain Emission Factors with Margins** based on DQ metrics and other parameters.
""")

# -----------------------------
# Input Form
# -----------------------------
with st.form("prediction_form"):
    substance = st.selectbox("Substance", ['carbon dioxide', 'methane', 'nitrous oxide', 'other GHGs'])
    unit = st.selectbox("Unit", ['kg/2018 USD, purchaser price', 'kg CO2e/2018 USD, purchaser price'])
    source = st.selectbox("Source", ['Commodity', 'Industry'])

    supply_wo_margin = st.number_input("Supply Chain Emission Factors without Margins", min_value=0.0)
    margin = st.number_input("Margins of Supply Chain Emission Factors", min_value=0.0)

    dq_reliability = st.slider("DQ Reliability", 0.0, 1.0)
    dq_temporal = st.slider("DQ Temporal Correlation", 0.0, 1.0)
    dq_geo = st.slider("DQ Geographical Correlation", 0.0, 1.0)
    dq_tech = st.slider("DQ Technological Correlation", 0.0, 1.0)
    dq_data = st.slider("DQ Data Collection", 0.0, 1.0)

    # Optional: year = st.selectbox("Year", list(range(2010, 2017)))

    submit = st.form_submit_button("Predict")

# -----------------------------
# Prediction Logic
# -----------------------------
if submit:
    try:
        input_data = {
            'Substance': substance,
            'Unit': unit,
            'Supply Chain Emission Factors without Margins': supply_wo_margin,
            'Margins of Supply Chain Emission Factors': margin,
            'DQ ReliabilityScore of Factors without Margins': dq_reliability,
            'DQ TemporalCorrelation of Factors without Margins': dq_temporal,
            'DQ GeographicalCorrelation of Factors without Margins': dq_geo,
            'DQ TechnologicalCorrelation of Factors without Margins': dq_tech,
            'DQ DataCollection of Factors without Margins': dq_data,
            'Source': source,
            # 'Year': year
        }

        input_df = preprocess_input(pd.DataFrame([input_data]))
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)

        st.success(f"📊 Predicted Supply Chain Emission Factor with Margin: **{prediction[0]:.4f} kg CO2e/USD**")

    except Exception as e:
        st.error(f"❌ Error occurred during prediction:\n\n{str(e)}")
