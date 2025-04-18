from flask import Flask, request, render_template, jsonify, redirect

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/loginData")
def loginData():
    """ zancmok magic
    if request.method == "GET":
        return render_template("signup.html")
    """

    username = request.args.get("username")
    password = request.args.get("password")

    print(username, type(username), bool(username))
    print(password, type(password), bool(password))

    # TODO replace "is True" and "is not True" with actual conditions(database needed)
    if username == True and password == True:
        print("e")

    if username == True and password == True:
        print("e")
        redirect("/index", code=302) #code 302 means permanent move
    
    if username == True and password != True:
        error = "Incorrect password"

    if username != True:
        error = "Incorrect username"

    return jsonify({"error": error})
    

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)