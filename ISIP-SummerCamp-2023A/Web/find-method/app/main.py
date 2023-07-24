# -*- coding:utf8 -*-
from flask import Flask, render_template, redirect, request, session,make_response
from base64 import b64encode
from datetime import timedelta

app = Flask(__name__,static_folder='static/')

@app.route("/",methods=["GET"])
def home():
    resp = make_response(render_template("blog.html"))
    resp.headers["Flag-From-Server"] = "FLAG{N0w_u_k0nw_g3t_method}"
    return resp
    

@app.route("/login",methods=["GET","POST"])
def login():
    errorMsg=""
    name = request.cookies.get('userID')
    if name == "admin":
        return redirect("/now-you-know-my-secret-path123",302)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "guest" and password=="guest":
            resp = make_response(render_template("panel.html",usern="guest"))
            resp.set_cookie("userID","FLAG{dont_st0r3_C00kie_in_c1i3nt}")
            return resp
        elif username == "tyc4d" and password=="password":
            resp = make_response(render_template("panel.html",usern="tyc4d"))
            resp.set_cookie("userID","tyc4d")
            return resp
        else:
            errorMsg='<div class="ts-notice is-negative u-top-spaced-large"><div class="title">密碼錯誤</div><div class="content">你會用開發者工具嗎?</div></div>'
            return render_template("login.html",errorMsg=errorMsg)
    return render_template("login.html",errorMsg=errorMsg)

@app.route("/now-you-know-my-secret-path123",methods=["GET"])
def admin_home():
    name = request.cookies.get('userID')
    if name == "admin":
        return render_template("panel.html",flagmsg="FLAG{dont_st0r3_C00kie_in_c1i3nt}")
    else:
        return redirect("/login",302)
@app.route("/logout",methods=["GET"])
def admin_logout():
    resp = make_response(redirect("/login",302))
    resp.delete_cookie("userID")
    return resp
    
@app.route("/api/user/delete/",methods=["DELETE"])
def admin_delete():
    if request.method == "DELETE":
        return "FLAG{u_f0und_4pi}"
    else:
        return "No Flag For U"


if __name__ == '__main__':
    app.run(debug=True)
