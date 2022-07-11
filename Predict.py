import joblib
mj = joblib.load("model_joblib.pkl")

# using the model object mj to make prediction
project = mj.predict([[2, 9147, 1, 3, 130.0, 1, 19, 1, 130.0, 1, 0, 0, 35, 0, 11.666667, 0, 11.333333]])
print (project)