from flask import Flask, request, render_template, jsonify, session
import bcrypt
import database_manager

app = Flask(__name__,)
app.config["SECRET_KEY"] = "Acrid" #afaik it just needs to be defined and youre done with it


@app.route("/")
def index():
    # TODO get rid of this session false later when you get a log out button
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
    # Doesnt matter if its false everytime since if someone wanna login then theyre probs logged out
    session["user_logged_in"] = False 

    # Checks if username is in db
    user_data: list[tuple | None] = database_manager.run_query("src/sql/search_user.sql", {"username": username})

    if not user_data:
        error = "Username doesn't exist"

    db_username = user_data[0][1]
    db_password = user_data[0][2]
    #idfk make password checking work
    if db_username == username and bcrypt.checkpw(password.encode("utf-8"), db_password.encode("utf-8")):
        error = "Incorrect password"
    
    if db_username == username and db_password == password:
        session["user_logged_in"] = True
        # TODO login works ish but sometime il have to send the info of the user to the main page or smth 

    return jsonify({"error": error,
                    "user_logged_in": session["user_logged_in"]})
    

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signupData", methods=["POST"])
def signupData():
    error = ""
    session["user_logged_in"] = False
    user_signed_up = False
    
    # Has to be request.form cuz post sends data in the body, not url
    username = request.form.get("username")
    password = request.form.get("password")

    # Checks username
    user_data: list[tuple | None] = database_manager.run_query("src/sql/search_user.sql", {"username": username})
    if user_data:
        error = "Username already exists"

    # Inserts the user into the database if theres no error
    if error == "":
        password_hash = hash_password(password)
        database_manager.execute("src/sql/insert_users.sql", {"username": username, "password": password_hash})
        user_signed_up = True
    
    print({"error": error, "user_signed_up": user_signed_up})

    return jsonify({"error": error, "user_signed_up": user_signed_up})


#GENERAL FUNCTIONS
def hash_password(password: str) -> str:
    # Converts password into bytes, generates salt and then hashes the password with the salt, converts hashed password back to string
    password_bytes: bytes = password.encode('utf-8') 
    salt: bytes = bcrypt.gensalt()
    password_hash: bytes = bcrypt.hashpw(password_bytes, salt)
    decoded_hash: str = password_hash.decode('utf-8')

    return decoded_hash

if __name__ == "__main__":
    app.run(debug=True)
