import pandas as pd
import numpy as np
import pickle
import json
import config

class Medical_insurance():
    def __init__(self,age ,sex ,bmi ,children ,smoker ,region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region=region
    
    def  load_model(self):
        with open(config.model_file_path , "rb") as f1:
            self.model=pickle.load(f1)

        with open(config.project_file_path , "r") as f2:
            self.project_data=json.load(f2)

    def get_medical_insurance(self):
        self.load_model()
        series=pd.Series(np.zeros(len(self.project_data['columns'])),index=self.project_data['columns'])
        series['age']=self.age
        series['sex']=self.project_data['sex'][self.sex]
        series['bmi']=self.bmi
        series['children']=self.children
        series['smoker']=self.project_data['smoker'][self.smoker]
        series['region']=self.project_data['region'][self.region]

        pred_output=self.model.predict([series])[0]
        pred_output=np.around(pred_output,4)
        insurance=f"Medical insurance charges is:{pred_output}"

        return insurance



# age=18
# sex='male'
# bmi=33.770
# children=1
# smoker='no'
# region='southwest'




