# -*- coding:utf8 -*-
from flask import Flask, render_template, redirect, request, session,make_response
from base64 import b64encode
from datetime import timedelta

app = Flask(__name__,static_folder='static/')

app.config.update(
TESTING=True,
SECRET_KEY=b'eere43443d',
SESSION_COOKIE_NAME="WHATDOUWANT",
#SESSION_COOKIE_DOMAIN=""
)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/",methods=["GET"])
def home():
    resp = make_response(render_template("blog.html"))
    resp.set_cookie("userID","FLAG{N0w_u_k0nw_g3t_method01}")
    return resp
    
@app.route("/magic_admin",methods=["GET"])
def magicadmin():
    name = request.cookies.get('userID')
    if name == "admin":
        return "FLAG{dont_st0r3_C00kie_in_c1i3nt}"
    else:
        return "No Flag For u"
    return "No Flag For u"

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
        else:
            errorMsg='<div class="ts-notice is-negative u-top-spaced-large"><div class="title">密碼錯誤</div><div class="content">你會用開發者工嗎?</div></div>'
    return render_template("login.html",errorMsg=errorMsg)

@app.route("/admin",methods=["GET"])
def admin_home():
    if session['login'] == 1:
        return render_template("panel.html")
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
    
@app.route("/api/user/delete/",methods=["DELETE"])
def admin_delete():
    return render_template("panel-user.html")


if __name__ == '__main__':
    app.run(debug=True)
