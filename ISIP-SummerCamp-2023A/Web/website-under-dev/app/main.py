# -*- coding:utf8 -*-
from flask import Flask, render_template, redirect, request, session,make_response
from base64 import b64encode
from datetime import timedelta
from flask_jwt_extended import JWTManager
cd ..
app = Flask(__name__,static_folder='static/')

app.config.update(
TESTING=True,
SECRET_KEY=b'eere43443d',
SESSION_COOKIE_NAME="UserID",
#SESSION_COOKIE_DOMAIN=""
)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/",methods=["GET"])
def home():
    resp = make_response(render_template("blog.html"))
    return resp
    

@app.route("/login",methods=["GET","POST"])
def login():
    errorMsg=""
    try:
        if 'login' not in session:
            session['login'] = 0
        if 'login_uid' not in session:
            session['login_uid'] = "X"
    except:
        print("?")
    if session['login'] == 1:
        return redirect("/admin")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password=="isipctf":
            session['login'] = 1
            session['login_uid'] = username
            return redirect("/admin",302)
        elif username == "guest" and password=="guest":
            session['login'] = 1
            session['login_uid'] = username
        else:
            errorMsg='<div class="ts-notice is-negative u-top-spaced-large"><div class="title">密碼錯誤</div><div class="content">你會用開發者工嗎?</div></div>'
    return render_template("login.html",errorMsg=errorMsg)

@app.route("/admin",methods=["GET"])
def admin_home():
    if session['login'] == 1 and session['login_uid'] == "admin":
        return render_template("panel.html")
    elif session['login'] == 1:
        return render_template("panel-user.html")
    else:
        return redirect("/login",302)
@app.route("/logout",methods=["GET"])
def admin_logout():
    if session['login'] == 1:
        session['login'] = 0
        session['login_uid'] = "X"
        return redirect("/login",302)
    else:
        return redirect("/login",302)
    

if __name__ == '__main__':
    app.run(debug=True)
