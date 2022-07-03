from flask import Flask, request, jsonify
import joblib

app = Flask (__name__)
# load the model, where mj = joblib model
mj = joblib.load("model_joblib.pkl")

@app.route("/")
@app.route("/index")
def home():
        """ Home View """

        return (jsonify(message="Hello, Welcome Home!"))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
        """
	    Predict View
	    Fit to suit your data/features
	    """
        #try:

            
        #request args
        Relationship = request.args.get('Marital_Status')
        if Relationship in ['Married']:
                Marital_Status = 2
        else:
                Marital_Status = 1

        Course = request.args.get('Course')

        ShowUp = request.args.get('Attendance')
        if ShowUp in ['Yes']:
                Attendance = 1
        else:
                Attendance = 0

        Qua  = request.args.get('Prev_Qua')

        if Qua in ['WAEC']:
                Prev_Qua = 1
        else:
                Prev_Qua = 0

        Prev_Qua_Grade = request.args.get('Prev_Qua_Grade')
        Region = request.args.get('Region')
        Mother_Qua = request.args.get('Mother_Qua')
        Father_Qua = request.args.get('Father_Qua')
        Adm_Grade = request.args.get('Adm_Grade')

        Fees = request.args.get('Tui_Up_to_Date')
        if Fees in ['Yes']:
                Tui_Up_to_Date = 1
        else:
                Tui_Up_to_Date =  0


        Status = request.args.get('Gender')
        if Status in ['Female']:
                Gender = 0
        else:
                Gender = 1

        Grant = request.args.get('S_Holder')
        if Grant in ['Yes']:
                S_Holder = 0
        else:
                S_Holder = 1

        Age_at_Enroll = request.args.get('Age_at_Enroll')
        Cur_U_1st_Sem_Credit = request.args.get('Cur_U_1st_Sem_Credit')
        Cur_U_1st_Sem_Grade = request.args.get('Cur_U_1st_Sem_Grade')
        Cur_U_2nd_Sem_Credit = request.args.get('Cur_U_2nd_Sem_Credit')
        Cur_U_2nd_Sem_Grade = request.args.get('Cur_U_2nd_Sem_Grade')

        #cast to int and float data type
        Marital_Status = int(Marital_Status)
        Course = int(Course)
        Attendance = int(Attendance)
        Prev_Qua = int(Prev_Qua)
        Prev_Qua_Grade = float(Prev_Qua_Grade)
        Region = int(Region)
        Mother_Qua = int(Mother_Qua)
        Father_Qua = int(Father_Qua)
        Adm_Grade = float(Adm_Grade)
        Tui_Up_to_Date = int(Tui_Up_to_Date)
        Gender = int(Gender)
        S_Holder = int(S_Holder)
        Age_at_Enroll = int(Age_at_Enroll)
        Cur_U_1st_Sem_Credit = int(Cur_U_1st_Sem_Credit)
        Cur_U_1st_Sem_Grade = float(Cur_U_1st_Sem_Grade)
        Cur_U_2nd_Sem_Credit = int(Cur_U_2nd_Sem_Credit)
        Cur_U_2nd_Sem_Grade = float(Cur_U_2nd_Sem_Grade)

		    #make prediction
        pred = mj.predict([[Marital_Status, Course, Attendance, Prev_Qua, Prev_Qua_Grade,
                                Region, Mother_Qua, Father_Qua, Adm_Grade, Tui_Up_to_Date, 
                                Gender, S_Holder, Age_at_Enroll, Cur_U_1st_Sem_Credit, 
                                Cur_U_1st_Sem_Grade, Cur_U_2nd_Sem_Credit,
                                Cur_U_2nd_Sem_Grade]]).tolist()
        return(jsonify(prediction=pred))
        #except:
                #return {"message":"ERROR!"}, 400

if __name__=="__main__":
    #debug=False for production use 
    app.run(debug=True, host='0.0.0.0', port=9001)
