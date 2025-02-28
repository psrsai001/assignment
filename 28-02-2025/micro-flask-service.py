from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello from home route"})


if __name__ == "__main__":
    app.run(port=4000)
