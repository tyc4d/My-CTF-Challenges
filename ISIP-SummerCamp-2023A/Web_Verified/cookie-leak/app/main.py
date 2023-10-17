# -*- coding:utf8 -*-
from flask import Flask, render_template, redirect, request, session,make_response
import jwt
app = Flask(__name__,static_folder='static/')

SECRETKEY="isipctf_key"

@app.route("/",methods=["GET"])
def home():
    resp = make_response(render_template("blog.html"))
    return resp
    

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Assuming a successful login, generate a JWT token
        if username == "admin" and password == "isipctf":
            jwt_token = jwt.encode({'username': username}, SECRETKEY, algorithm='HS256')
            resp = make_response(redirect("/admin"))
            resp.set_cookie('jwt_token', jwt_token)
            return resp
        elif username == "guest" and password == "guest":
            jwt_token = jwt.encode({'username': username}, SECRETKEY, algorithm='HS256')
            resp = make_response(redirect("/admin"))
            resp.set_cookie('jwt_token', jwt_token)
            return resp
        else:
            errorMsg='<div class="ts-notice is-negative u-top-spaced-large"><div class="title">密碼錯誤</div><div class="content">你會用開發者工嗎?</div></div>'
            return render_template("login.html", errorMsg=errorMsg)
    else:
        return render_template("login.html")


@app.route("/admin", methods=["GET"])
def admin_home():
    jwt_token = request.cookies.get('jwt_token')
    try:
        jwt_data = jwt.decode(jwt_token, SECRETKEY, algorithms=['HS256'])
        username = jwt_data['username']
        if username == "admin":
            return render_template("panel.html")
        else:
            return render_template("panel-user.html")
    except jwt.ExpiredSignatureError:
        return redirect("/login", 302)  # Token has expired
    except jwt.DecodeError:
        return redirect("/login", 302)  # Token is invalid

@app.route("/logout", methods=["GET"])
def admin_logout():
    resp = make_response(redirect("/login"))
    resp.delete_cookie('jwt_token')
    return resp

    

if __name__ == '__main__':
    app.run(debug=True)