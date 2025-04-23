from flask import Flask, request, render_template, jsonify, redirect, session

app = Flask(__name__,)
app.config["SECRET_KEY"] = "Acrid" #afaik it just needs to be defined and youre done with it


@app.route("/")
def index():
    #TODO get rid of this session false later
    session["user_logged_in"] = False
    return render_template("index.html")


@app.route("/login")
def login():
    """not needed for now or ever
    if session.get("user_logged_in"):
        return redirect("/")"""

    return render_template("login.html")

@app.route("/loginData", methods=["GET"])
def loginData():
    username = request.args.get("username")
    password = request.args.get("password")

    error = ""
    session["user_logged_in"] = False #doesnt matter if its false everytime since if someone wanna login then theyre logged out

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
    print("2")
    return render_template("signup.html")

@app.route("/signupData", methods=["POST"])
def signupData():
    print("1")
    username = request.args.get("username")
    password = request.args.get("password")

    error = ""
    session["user_logged_in"] = False

    # TODO put actual conditions in (database needed)
    if not username:
        error = "Username already exists"


    #put user into database or smth
    user_signed_up = True
    print({"error": error, "user_signed_up": user_signed_up})

    return jsonify({"error": error, "user_signed_up": user_signed_up})

if __name__ == "__main__":
    app.run(debug=True)
