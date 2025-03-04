from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "hello wold"}


@app.route("/list")
def list():
    return render_template("count_list.html", items=[1, 2, 3])


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email is None or password is None:
            return (jsonify({"message": "Invalid inputs."}), 400)
        print(password, email)
        return (jsonify({"email": email, "password": "******"}), 201)

    return jsonify({"message": "Invalid request"}), 400


@app.route("/even")
def even():
    return redirect(url_for("home"))


@app.route("/odd")
def odd():
    return "<h1>This is the odd page</h1>"
