from flask import Flask, request, render_template, jsonify, session
import bcrypt
import database_manager

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

    print(username, password)

    error = ""
    session["user_logged_in"] = False

    # TODO put actual conditions in (database needed)
    if not username:
        error = "Username already exists"

    #inserts the user into the database
    if error == "":
        #converts password into bytes, generates salt and then hashes the password with the salt, converts hashed password back to string(for db)
        password_bytes: bytes = password.encode('utf-8') 
        salt: bytes = bcrypt.gensalt()
        password_hash: bytes = bcrypt.hashpw(password_bytes, salt)
        decoded_hash: str = password_hash.decode('utf-8')

        #insert
        database_manager.run_query("src/sql/insert_users.sql", {"username": username, "password": decoded_hash})

        user_signed_up = True

    
    print({"error": error, "user_signed_up": user_signed_up})

    return jsonify({"error": error, "user_signed_up": user_signed_up})

if __name__ == "__main__":
    app.run(debug=True)
