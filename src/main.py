from flask import Flask, request, render_template, jsonify, session
from database_manager import func1

app = Flask(__name__,)
app.config["SECRET_KEY"] = "Acrid" #afaik it just needs to be defined and youre done with it


@app.route("/")
def index():
    #TODO get rid of this session false later when you get a log out button
    session["user_logged_in"] = False
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginData", methods=["POST"])
def loginData():
    username = request.form.get("username")
    password = request.form.get("password")

    error = ""
    #doesnt matter if its false everytime since if someone wanna login then theyre probs logged out
    session["user_logged_in"] = False 

    # TODO put actual conditions in (database needed)
    if username and password:
        session["user_logged_in"] = True
    
    if username and not password:
        error = "Incorrect password"

    if not username:
        error = "Incorrect username"

    return jsonify({"error": error,
                    "user_logged_in": session["user_logged_in"]})
    

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signupData", methods=["POST"])
def signupData():
    #has to be request.form cuz post sends data in the body, not url
    username = request.form.get("username")
    password = request.form.get("password")

    error = ""
    session["user_logged_in"] = False

    # TODO put actual conditions in (database needed)
    if not username:
        error = "Username already exists"

    
    # TODO put user into database or smth


    user_signed_up = True
    print({"error": error, "user_signed_up": user_signed_up})

    return jsonify({"error": error, "user_signed_up": user_signed_up})

if __name__ == "__main__":
    app.run(debug=True)
