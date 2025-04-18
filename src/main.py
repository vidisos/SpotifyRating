from flask import Flask, request, render_template, jsonify, redirect, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    if session.get("user_logged_in"):
        return redirect("/")

    return render_template("login.html")

@app.route("/loginData", methods=["GET"])
def loginData():
    username = request.args.get("username")
    password = request.args.get("password")

    # TODO put actual conditions in (database needed)
    if username and password:
        session["user_logged_in"] = True
        error = ""
    
    if username and not password:
        error = "Incorrect password"

    if username:
        error = "Incorrect username"

    return jsonify({"error": error})
    

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.config["SECRET_KEY"] = "sigma"

    app.run(debug=True)
