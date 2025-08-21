# Loan Approval Prediction App

This is a Machine Learning project to predict loan approval status based on applicant information.  
The model was trained using classification algorithms (XGBoost, Logistic Regression, etc.) and deployed as an interactive web app using **Streamlit**.

🔗 **Live Demo:** [Click here to try the app](OTW)

---

## 📊 Features
- Predicts loan approval based on:
  - Number of dependents
  - Applicant income
  - Loan amount
  - Loan term
  - CIBIL score
  - Assets values
  - Education level
  - Employment status
- User-friendly web interface (Streamlit)

---

## 🛠 Tech Stack
- Python
- Scikit-learn
- XGBoost
- Streamlit
- Pandas & Numpy

---

## 🚀 Deployment
The app is deployed on **Streamlit Cloud**.  
To run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
