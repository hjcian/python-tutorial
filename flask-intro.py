from flask import Flask

app = Flask(__name__)

# endpoint / router
# http://localhost/
# decorator 裝飾器 ／ 修飾器
# 定義
@app.route("/") # 就是一般而言的首頁
def hello():
    # endpoint
    print("Hello")
    print("World")
    return "Hello, World!"

@app.route("/a/b/c.htm") # 就是一般而言的首頁
def foo():
    # endpoint
    print("foo")
    print("bar")
    return "foo, bar!"

if __name__ == "__main__":
    print("Start server")

    host = "localhost" # 開放給所有人都可以連
    port = 3456

    app.run(host=host, port=port)
    print("Server shutdonw")