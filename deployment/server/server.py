from flask import Flask, request,render_template, redirect, url_for, session
from util import make_prediction
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        age_data = int(request.form['age'])
        capital_gain_data = int(request.form['capital_gain'])
        capital_loss_data = int(request.form['capital_loss'])
        hour_data = int(request.form['hour'])
        education_data = request.form['education']
        workclass_data = request.form['workclass']
        occupation_data = request.form['occupation']

        predicted_value = make_prediction(age=age_data, capital_gain=capital_gain_data, capital_loss=capital_loss_data, education=education_data,
                        hour_per_week=hour_data, workclass=workclass_data, occupation=occupation_data)

        return redirect(url_for('result', predicted_value=predicted_value))

    return render_template('home.html')

@app.route("/result", methods = ['GET', 'POST'])
def result():

    prediction = request.args.get('predicted_value')

    return render_template('result.html', predicted_value = prediction)







if __name__ == "__main__":
    app.run(debug = True)
