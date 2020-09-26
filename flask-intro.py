from flask import Flask
from flask import request
from flask import Response
import json


app = Flask(__name__) 

#@就是 decorator 裝飾器 / 修飾器
#反正就是寫上去
@app.route("/") # 就是一般而言的首頁
def hello():
    return "Hello, World!"

#上面都只是定義
@app.route("/a/b/c.htm") # 就是一般而言的首頁
def foo():
    return "123, 333!"

@app.route("/a/a/a.htm") # 就是一般而言的首頁
def fooaa():
    return "aaa!"

#USERS = {} #dict
#{}

if __name__ == "__main__":
    print("Start server")

    host = "0.0.0.0"  #開放給所有人都可以連 改localhost 就只有自己可以連
    port = 3456

    app.run(host=host, port=port,debug=True)
    print("Server shutdonw")