import flask
from flask import Flask, render_template, url_for, request
import pandas as pd, numpy as np
import pickle

# load the model from disk
filename = 'RandomForest.pkl'
clf = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@ app.route('/')
def heart_disease_prediction():
    title = 'Early Heart Disease Prediction'
    return render_template('index.html', title=title)

@ app.route('/disease-predict', methods=['POST'])
def disease_prediction():
    title = 'Early Heart Disease Prediction'

    if request.method == 'POST':
        a = int(request.form['age'])
        s = int(request.form['sex'])
        cp = int(request.form['cp'])
        tr = int(request.form['trestbps'])
        ch = int(request.form['chol'])
        f = int(request.form['fbs'])
        r = int(request.form['restecg'])
        th = int(request.form['thalach'])
        e = int(request.form['exang'])
        o = float(request.form['oldpeak'])
        sl = int(request.form['slope'])
        c = int(request.form['ca'])
        thl = int(request.form['thal'])

        data = np.array([[ a , s , cp , tr , ch , f , r , th , e , o , sl , c , thl]])
        my_prediction = clf.predict(data)
        print(my_prediction[0])
        if my_prediction[0] == 0:
            sentence = "You won't have any heart disease."
        else:
            sentence = "You might have a heart disease."
        return render_template('index.html', prediction=sentence, title=title)


if __name__ == '__main__':
	app.run(debug=True)