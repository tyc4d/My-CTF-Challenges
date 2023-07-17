from flask import Flask, render_template, redirect, request, g
from base64 import b64encode

app = Flask(__name__)


@app.route("/",methods=["GET"])
def home():
    return render_template("blog.html")

@app.route("/login",methods=["GET"."POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password=="isipctf":
            return red
    return render_template("login.html",failed=request.args.get('failed') != None)

@app.route("/admin",methods=["GET"])
def admin_home():
    return render_template("blog.html")
    
@app.route("/api/user/delete",methods=["GET","DELETE"])
def admin_delete():
    return render_template("blog.html")


if __name__ == '__main__':
    app.run(debug=True)
