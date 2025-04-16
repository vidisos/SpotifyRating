from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


app.run(debug=True)