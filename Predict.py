import joblib
mj = joblib.load("model_joblib.pkl")

# using the model object mj to make prediction

project = mj.predict([[2, 9130, 1, 3, 136.0, 1, 3, 38, 119.8, 1, 1, 0, 18, 10, 12, 11.571429, 0, 6, 12.142857]])
print (project)