# -*- coding:utf8 -*-
from flask import Flask, render_template, redirect, request, make_response

app = Flask(__name__,static_folder='static/')

@app.route("/",methods=["GET"])
def home():
    resp = make_response(render_template("index.html"))
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
        # Hardcoded Username And Password
        if username == "guest" and password=="guest":
            resp = make_response(render_template("panel.html",usern="guest"))
            resp.set_cookie("userID","guest")
            resp.set_cookie("userSpecialData","FLAG{dont_st0r3_C00kie_in_c1i3nt}")
            return resp
        elif username == "admin":
            errorMsg = '<div class="ts-notice is-negative u-top-spaced-large"><div class="title">此帳號已停用</div><div class="content">P.S. 試試看先登入其他帳號?</div></div>'
            return render_template("login.html",errorMsg=errorMsg)
        else:
            errorMsg='<div class="ts-notice is-negative u-top-spaced-large"><div class="title">密碼錯誤</div><div class="content">P.S. 你會用開發者工具嗎?</div></div>'
            return render_template("login.html",errorMsg=errorMsg)
    return render_template("login.html",errorMsg=errorMsg)

@app.route("/now-you-know-my-secret-path123",methods=["GET"])
def admin_home():
    name = request.cookies.get('userID')
    if name == "admin":
        return render_template("panel-flag.html",usern=name,flagmsg="FLAG{dont_st0r3_C00kie_in_c1i3nt}")
    else:
        return redirect("/login",302)
@app.route("/logout",methods=["GET"])
def admin_logout():
    resp = make_response(redirect("/login",302))
    resp.delete_cookie("userID")
    resp.delete_cookie("userSpecialData")
    return resp
    
if __name__ == '__main__':
    app.run(debug=True)
