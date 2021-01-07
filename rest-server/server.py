from flask import Flask
from flask import request
from flask import Response
import json

app = Flask(__name__)


DB = {
    "maxcian": 1000
}


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/login', methods=['POST'])
def login():
    return "Token"  # 驗證

# middleware ("check Token if valid")
# login verification
# JWT (JSON Web token)


@app.route('/delete/<username>', methods=['DELETE'])
def delete(username):
    del DB[username]
    pass


@app.route('/register', methods=['POST'])
def register():
    # 1. 如何拿到 request 的內容
    # 2. 根據內容(username's value)，存到 DB
    # 3. reply 適合的回應給用戶端
    req = request.get_json()

    user = req.get("username")
    if not user:
        return Response(
            response=json.dumps({
                "errmsg": "username is invalid"
            }),
            status=400,
            content_type="application/json"
        )

    # DB 裡重複 user
    if user in DB:
        return Response(
            response=json.dumps({
                "errmsg": "username is exists"
            }),
            status=406,
            content_type="application/json"
        )
    print(user)
    DB[user] = 0  # 新使用者，存款為０

    return Response(
            response=json.dumps({
                "msg": "OK"
            }),
            status=200,
            content_type="application/json"
        )


@app.route("/balance/<username>", methods=["GET"])
def balance(username):

    if username not in DB:
        return Response(
            response=json.dumps({
                "errmsg": "username not found"
            }),
            status=404,
            content_type="application/json"
        )

    balance = DB[username]

    return Response(
            response=json.dumps({
                "balance": balance
            }),
            status=200,
            content_type="application/json"
        )


@app.route("/deposit/<username>", methods=["POST"])
def deposit(username):
    req = request.get_json()
    amount = req.get("amount")

    if amount < 0:
        pass

    if username not in DB:
        pass

    DB[username] += amount

    balance = DB[username]

    return Response(
            response=json.dumps({
                "balance": balance
            }),
            status=200,
            content_type="application/json"
        )


if __name__ == "__main__":
    print("Start server")

    host = "0.0.0.0"
    port = 3456

    app.run(host=host, port=port, debug=True)
    print("Server shutdown")
