from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/<user_name>")
def greet_user(user_name):
    return f"Hello, {user_name}"


@app.route("/inject/<htm>")
def inject(htm):
    return htm


@app.route("/scores/<int:score>")
def score(score: int):
    return f"{ score }"


if __name__ == "__main__":
    app.debug = True
    app.run()
