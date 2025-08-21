import streamlit as st
import joblib
import numpy as np

# load model
model = joblib.load("loan_approval_model.pkl")

st.title("Loan Approval Prediction App")

# numerical inputs
no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, step=1)
income_annum = st.number_input("Applicant Annual Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (in months)", min_value=1, max_value=360)
cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900)
residential_assets_value = st.number_input("Residential Assets Value", min_value=0)
commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0)
luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0)
bank_asset_value = st.number_input("Bank Asset Value", min_value=0)

# categorical inputs
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

if st.button("Predict Loan Approval"):
    # one-hot encoding sesuai dengan dataset
    education_graduate = 1 if education == "Graduate" else 0
    education_not_graduate = 1 if education == "Not Graduate" else 0
    self_employed_yes = 1 if self_employed == "Yes" else 0
    self_employed_no = 1 if self_employed == "No" else 0

    # susun input sesuai urutan kolom dataset
    features = np.array([[
        no_of_dependents,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value,
        education_graduate,
        education_not_graduate,
        self_employed_no,
        self_employed_yes
    ]])

    prediction = model.predict(features)[0]
    
    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

