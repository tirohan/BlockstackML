import streamlit as st
import pandas as pd
from joblib import load
import pickle
from sklearn.preprocessing import LabelEncoder

with open('./model_files/decision_tree_model.pkl', 'rb') as dt_file:
    dt_model = pickle.load(dt_file)

with open('./model_files/naive_bayes_model.pkl', 'rb') as nb_file:
    nb_model = pickle.load(nb_file)

df = pd.read_csv('./Bank_data.csv')

label_encoder_job = LabelEncoder()
label_encoder_marital = LabelEncoder()
label_encoder_education = LabelEncoder()
label_encoder_default = LabelEncoder()
label_encoder_housing = LabelEncoder()
label_encoder_loan = LabelEncoder()
label_encoder_contact = LabelEncoder()
label_encoder_month = LabelEncoder()
label_encoder_poutcome = LabelEncoder()

label_encoder_job.fit(df['job'])
label_encoder_marital.fit(df['marital'])
label_encoder_education.fit(df['education'])
label_encoder_default.fit(df['default'])
label_encoder_housing.fit(df['housing'])
label_encoder_loan.fit(df['loan'])
label_encoder_contact.fit(df['contact'])
label_encoder_month.fit(df['month'])
label_encoder_poutcome.fit(df['poutcome'])

st.title("Predictive Model")

age = st.number_input("Age", min_value=0, value=30)
balance = st.number_input("Balance", min_value=0, value=1000)
duration = st.number_input("Duration", min_value=0, value=100)
campaign = st.number_input("Campaign", min_value=0, value=1)
previous = st.number_input("Previous", min_value=0, value=0)

job = st.selectbox("Job", list(df['job'].unique()))
marital = st.selectbox("Marital", list(df['marital'].unique()))
education = st.selectbox("Education", list(df['education'].unique()))
default = st.selectbox("Default", list(df['default'].unique()))
housing = st.selectbox("Housing", list(df['housing'].unique()))
loan = st.selectbox("Loan", list(df['loan'].unique()))
contact = st.selectbox("Contact", list(df['contact'].unique()))
month = st.selectbox("Month", list(df['month'].unique()))
poutcome = st.selectbox("Poutcome", list(df['poutcome'].unique()))
selected_model = st.selectbox("Select Model", ["Decision Tree", "Naive Bayes"])


if st.button("Predict"):
    # Encode categorical variables
    job_encoded = label_encoder_job.transform([job])
    marital_encoded = label_encoder_marital.transform([marital])
    education_encoded = label_encoder_education.transform([education])
    default_encoded = label_encoder_default.transform([default])
    housing_encoded = label_encoder_housing.transform([housing])
    loan_encoded = label_encoder_loan.transform([loan])
    contact_encoded = label_encoder_contact.transform([contact])
    month_encoded = label_encoder_month.transform([month])
    poutcome_encoded = label_encoder_poutcome.transform([poutcome])

    input_data = [[age, balance, duration, campaign, previous, job_encoded[0], marital_encoded[0], education_encoded[0], default_encoded[0], housing_encoded[0], loan_encoded[0], contact_encoded[0], month_encoded[0], poutcome_encoded[0]]]

    if selected_model == "Decision Tree":
        prediction = dt_model.predict(input_data)[0]
    elif selected_model == "Naive Bayes":
        prediction = nb_model.predict(input_data)[0]

    st.write(f"Prediction: {prediction}")