import joblib
import pickle

# Load your .joblib models
dt_model = joblib.load('decision_tree_model.joblib')
nb_model = joblib.load('naive_bayes_model.joblib')

# Save the models in pickle format
with open('decision_tree_model.pkl', 'wb') as dt_file:
    pickle.dump(dt_model, dt_file)

with open('naive_bayes_model.pkl', 'wb') as nb_file:
    pickle.dump(nb_model, nb_file)