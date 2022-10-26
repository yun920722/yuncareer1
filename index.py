from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>黃品芸的求職資訊網頁</h1>"
    homepage += "<a href=/me>自我介紹</a><br>"
    return homepage

@app.route("/me")
def route():
    return render_template("me.html")

#if __name__ == "__main__":
#    app.run()