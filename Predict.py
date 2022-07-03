import joblib
mj = joblib.load("model_joblib.pkl")

# using the model object mj to make prediction
project = mj.predict([[2, 8, 1, 0, 130.0, 4, 5, 5, 130.0, 1, 1, 0, 18, 0, 11.666667, 0, 11.333333]])
print (project)