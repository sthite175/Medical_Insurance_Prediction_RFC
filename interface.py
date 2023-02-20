from flask import Flask,render_template,request
from utilities import Medical_insurance
import config

app=Flask(__name__)
@app.route("/")
def app_home():
    return render_template("index.html")

@app.route("/prediction" , methods=["post"])
def get_med_insurance():
    data=request.form
    age=float(data['age'])
    sex=data['sex']
    bmi=float(data['bmi'])
    children=float(data['children'])
    smoker=data['smoker']
    region=data['region']

    instance=Medical_insurance(age,sex,bmi,children,smoker,region)
    charges=instance.get_medical_insurance()

    return render_template("index.html" , Result=charges)  # It will get the output

# For code run
if __name__=="__main__":
    app.run(debug=True , port=config.PORT , host=config.HOST)


