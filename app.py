import streamlit as st
import numpy as np
import joblib

# ------------------------------------------------------------
# Load model (cached so it only loads once)
# ------------------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load("salary_model.pkl")

model = load_model()

# ------------------------------------------------------------
# Page setup
# ------------------------------------------------------------
st.set_page_config(page_title="Salary Predictor", page_icon="💰")
st.title("💰 Salary Predictor")
st.write("Enter years of experience to predict expected salary.")

# ------------------------------------------------------------
# Input form
# ------------------------------------------------------------
years_experience = st.number_input(
    "Years of Experience", min_value=0.0, max_value=50.0, value=5.0, step=0.5
)

if st.button("Predict Salary"):
    input_arr = np.array([[years_experience]])
    prediction = model.predict(input_arr)[0]
    st.success(f"Predicted Salary: **${prediction:,.2f}**")
