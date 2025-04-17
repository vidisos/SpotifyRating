from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/loginData", methods=["GET", "POST"])
def loginData():
    """
    if request.method == "GET":
        return render_template("signup.html")
    """

    username = request.args.get("username")
    password = request.args.get("password")

    print(username)
    print(password)

    if username is True and password is True:
        return render_template("index.html")
    
    if username is True and password is not True:
        error = "Incorrect password"

    if username is not True:
        error = "Incorrect username"

    return jsonify({"error": error})
    

@app.route("/signup")
def signup():
    return render_template("signup.html")


app.run(debug=True)