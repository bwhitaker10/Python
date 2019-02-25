from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Wassup"


@app.route('/')
def index():
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

@app.route('/increase', methods=['POST'])
def increase():
    session['counter'] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session['counter'] = 0
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)