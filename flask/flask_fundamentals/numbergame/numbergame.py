import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Wassup"


@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    if 'result' not in session:
        session['result'] = 'Good Luck!'
    return render_template("index.html", result=session['result'])

@app.route('/prediction', methods=['POST'])
def prediction():
    prediction=int(request.form['number'])
    if prediction == session['number']:
        session['result'] = f"{session['number']} Correct!"
    if prediction > session['number']:
        session['result'] = "Too High!"
    elif prediction < session['number']:
        session['result'] = "Too Low!"
    return redirect('/')

@app.route('/startover')
def startover():
    session['number']
    session.pop('number')
    session.pop('result')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)