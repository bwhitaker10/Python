from flask import Flask, render_template, request
app = Flask(__name__)
app.secret_key = "Wassup"
# our index route will handle rendering our form


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print("Got Post Info")
    print(request.form)
    return render_template("result.html", name=request.form["name"], dojolocation=request.form["dojolocation"], favlanguage=request.form["favlanguage"], comment=request.form["comment"])

if __name__ == "__main__":
    app.run(debug=True)