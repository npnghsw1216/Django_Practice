from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    # DB Aceess
    like_foods = ["김치찌개", "된장찌개", "밥", "고기", "짜장면", "짬뽕"]
    return render_template("profile.html", like_foods=like_foods)


@app.route("/posts")
def post_list():
    return render_template("post_list.html")
