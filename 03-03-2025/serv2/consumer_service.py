import os

import requests
from flask import Flask

URL = os.getenv("URL", "127.0.0.1")
PORT = os.getenv("PORT", "3000")


def get_rand_int():
    res = requests.get(f"http://{URL}:{PORT}/number")
    data: dict[str, int] = res.json()
    rand_num = data.get("number", None)
    return rand_num


app = Flask(__name__)


@app.route("/rand-num")
def rand_num():
    n = get_rand_int()
    if n is None:
        return {"error": "Unable to get the number"}
    return {"consumer_num": n}, 500


if __name__ == "__main__":
    app.run(debug=True, port=3001)
