from flask import Flask, request
from flask import Response

import json

app = Flask(__name__)

USERS = {
    "max": 0
}


@app.route('/')
def hello():
    return "hello world!"


@app.route('/register', methods=['POST'])
def register():
    req = request.get_json()
    username = req.get("username")

    if not username:
        # return "NG"
        # return "NG", 400
        return Response(
            status=400,
            response=json.dumps({
                "msg": "need username"
            }),
            mimetype="application/json",
        )

    if username in USERS:
        # return "user {} exists".format(username)
        # return "user {} exists".format(username), 406
        return Response(
            status=406,
            response=json.dumps({
                "msg": "user exists"
            }),
            mimetype="application/json",
        )

    USERS[username] = 0
    # return "register OK"
    # return "register OK", 200
    return Response(
        status=200,
        response=json.dumps({
            "msg": "OK"
        }),
        mimetype="application/json",
    )


@app.route("/balance/<username>", methods=['GET'])
def balance(username):
    if username not in USERS:
        return Response(
            status=404,
            response=json.dumps({
                "msg": "user not found"
            }),
            mimetype="application/json",
        )

    return Response(
        status=200,
        response=json.dumps({
            "msg": "OK",
            "balance": USERS[username]
        }),
        mimetype="application/json",
    )


@app.route("/deposit/<username>", methods=['POST'])
def deposit(username):

    if username not in USERS:
        return Response(
            status=404,
            response=json.dumps({
                "msg": "user not found"
            }),
            mimetype="application/json",
        )

    req = request.get_json()
    amount = req.get("amount")
    if not amount:
        return Response(
            status=400,
            response=json.dumps({
                "msg": "need amount"
            }),
            mimetype="application/json",
        )

    USERS[username] += amount

    return Response(
        status=200,
        response=json.dumps({
            "msg": "deposit OK",
        }),
        mimetype="application/json",
    )


if __name__ == "__main__":
    print("Start server")

    host = "0.0.0.0"
    port = 8888

    app.run(host=host, port=port, debug=True)

    print("Server shutdonw")
