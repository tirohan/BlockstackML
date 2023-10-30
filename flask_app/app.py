from flask import Flask, render_template, request
from joblib import load
from sklearn.preprocessing import LabelEncoder
import pandas as pd 

app = Flask(__name__)


dt_model = load('./model_files/decision_tree_model.joblib')

nb_model = load('./model_files/naive_bayes_model.joblib')

df = pd.read_csv('./Bank_data.csv')

# Define and fit LabelEncoder objects for categorical features (already fitted)
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input data from the form
        age = float(request.form['age'])
        balance = float(request.form['balance'])
        duration = float(request.form['duration'])
        campaign = float(request.form['campaign'])
        previous = float(request.form['previous'])
        job = request.form['job']
        marital = request.form['marital']
        education = request.form['education']
        default = request.form['default']
        housing = request.form['housing']
        loan = request.form['loan']
        contact = request.form['contact']
        month = request.form['month']
        poutcome = request.form['poutcome']

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

        # Prepare the input data for predictions
        input_data = [[age, balance, duration, campaign, previous, job_encoded[0], marital_encoded[0], education_encoded[0], default_encoded[0], housing_encoded[0], loan_encoded[0], contact_encoded[0], month_encoded[0], poutcome_encoded[0]]]

        # Get the selected model from the dropdown
        selected_model = request.form['model_select']

        # Perform predictions based on the selected model
        if selected_model == 'decision_tree':
            prediction = dt_model.predict(input_data)[0]
        elif selected_model == 'naive_bayes':
            prediction = nb_model.predict(input_data)[0]

        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)