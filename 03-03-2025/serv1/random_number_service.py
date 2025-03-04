import random

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/number", methods=["GET"])
def send_a_number():
    number = random.randint(1, 20)
    return {"number": number}


if __name__ == "__main__":
    app.run(port=3000)
