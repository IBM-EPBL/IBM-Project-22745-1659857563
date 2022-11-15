from flask import Flask, render_template
app = Flask(__name__)
app.secret_key="hello"

@app.route("/")
def homepage():
	return render_template("home.html")


@app.route("/addstock")
def add():
    return render_template("addstock.html")
	
@app.route("/dashboard")                                      
def dashboard():
	return render_template("dashboard.html")

@app.route("/deletestock")
def delete():
    return render_template("deletestock.html")

@app.route("/update_stock")
def update():
    return render_template("update_stock.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/view")
def view():
    return render_template("view.html")

if __name__ =="__main__":
    app.run(debug=True)