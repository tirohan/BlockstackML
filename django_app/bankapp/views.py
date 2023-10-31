from django.shortcuts import render
from django.http import HttpResponse, JsonResponse  
from joblib import load
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load models and preprocessors
dt_model = load('D:/BlockStack/django_app/bankapp/model_files/decision_tree_model.joblib')
nb_model = load('D:/BlockStack/django_app/bankapp/model_files/naive_bayes_model.joblib')
df = pd.read_csv('D:/BlockStack/django_app/bankapp/Bank_Data.csv')

# Label encoders
label_encoders = {}  

categorical_features = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']

for feature in categorical_features:
    label_encoder = LabelEncoder()
    label_encoder.fit(df[feature])
    label_encoders[feature] = label_encoder

def index(request):
    return render(request, 'bankapp/index.html')

def predict(request):
    if request.method == 'POST':
        try:
            # Process form data
            age = float(request.POST['age'])
            balance = float(request.POST['balance'])
            duration = float(request.POST['duration'])
            campaign = float(request.POST['campaign'])
            previous = float(request.POST['previous'])
            job = request.POST['job']
            marital = request.POST['marital']
            education = request.POST['education']
            default = request.POST['default']
            housing = request.POST['housing']
            loan = request.POST['loan']
            contact = request.POST['contact']
            month = request.POST['month']
            poutcome = request.POST['poutcome']

            # Transform categorical variables using label encoders
            job_encoded = label_encoders['job'].transform([job])[0]
            marital_encoded = label_encoders['marital'].transform([marital])[0]
            education_encoded = label_encoders['education'].transform([education])[0]
            default_encoded = label_encoders['default'].transform([default])[0]
            housing_encoded = label_encoders['housing'].transform([housing])[0]
            loan_encoded = label_encoders['loan'].transform([loan])[0]
            contact_encoded = label_encoders['contact'].transform([contact])[0]
            month_encoded = label_encoders['month'].transform([month])[0]
            poutcome_encoded = label_encoders['poutcome'].transform([poutcome])[0]

            input_data = [[age, balance, duration, campaign, previous, job_encoded, marital_encoded, education_encoded, default_encoded, housing_encoded, loan_encoded, contact_encoded, month_encoded, poutcome_encoded]]

            selected_model = request.POST['model_select']

            if selected_model == 'decision_tree':
                prediction = dt_model.predict(input_data)[0]
            elif selected_model == 'naive_bayes':
                prediction = nb_model.predict(input_data)[0]

            return render(request, 'bankapp/prediction.html', {'prediction': prediction})

        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Method not allowed'})
