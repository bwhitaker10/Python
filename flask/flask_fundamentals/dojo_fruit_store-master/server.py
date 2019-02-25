from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    fruits = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {fruits} fruits")
    print(request.form)
    return render_template("checkout.html", strawberry=request.form["strawberry"], raspberry=request.form["raspberry"], apple=request.form["apple"], firstname=request.form["first_name"], lastname=request.form["last_name"], student_id=request.form["student_id"])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)

# No. 4: I noticed a GET intead of POST when refreshing the checkout. The page did not run.