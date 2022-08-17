from asyncore import readwrite
from cProfile import run
from logging import debug
import pickle
from flask import Flask,render_template,request
import numpy as np

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods= ['GET','POST'])
def predict():
            age=float(request.form.get('age',False))
            sex= float(request.form.get('sex',False))
            
            chol=float(request.form.get('chol',False))
           
            thalach= float(request.form.get('thalachh',False))
           

            arr=np.array([[age,sex,chol,thalach]])
            pred=model.predict(arr)
            if pred==0:
                res_Val="No heart problem,Your Doing Good"
            else:
                res_Val="Heart Problem,You may have to give extra care towards your health"

            return render_template('result.html',prediction_text='Patient has {}'.format(res_Val))


if __name__=='__main__':
    app.run(debug=True)