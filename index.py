from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>黃品芸的求職資訊網頁</h1>"
    homepage += "<a href=/me>自我介紹</a><br>"
    homepage += "<a href=/mis>MIS工作介紹</a><br>"
    homepage += "<a href=/career>職涯測驗結果</a><br>"
    homepage += "<a href=/me1>求職自傳</a><br>"
    return homepage

@app.route("/me")
def route():
    return render_template("me.html")
@app.route("/mis")
def mis():
    return render_template("mis.html")
@app.route("/career")
def career():
    return render_template("career.html")
@app.route("/me1")
def me1():
    return render_template("me1.html")

#if __name__ == "__main__":
#    app.run()