
from flask import Flask,redirect,url_for,render_template,request,Response,flash,session
from form import form
from login import login
import re

app=Flask(__name__)
app.secret_key="oiut9^45$67"
validate_user=[
    {"name":"MOHANAPAL",
    'password':"123$lktuier"},
    {"name":"MRITTIKAPAL",
    'password':"12$lktuier"},
    {"name":"DEYAROY",
    'password':"123$lk567"},
    {"name":"MIKASAACKERMAN",
    'password':"ghtji590"},
    
]

@app.route("/",methods=['GET',"POST"])
def loginform():
    loginForm=login()
    if loginForm.validate_on_submit():
        Name=loginForm.Name.data
        password=loginForm.Password.data
        value=re.sub(r"\s+","",Name).strip().upper()
        for i in validate_user:
            if value==i["name"] and password==i['password']:
                session["user"]=value
                return redirect(url_for("reg"))
        else:
            return Response("Invalid Password",mimetype="text/plain")


    return render_template("login.html",loginForm=loginForm)

            

@app.route("/reg",methods=["GET","POST"])
def reg():
    if "user" not in session:
        return redirect(url_for("loginform"))
    else:
        RegForm=form()
        if RegForm.validate_on_submit():
            name=RegForm.Name.data
            value=re.sub(r"\s+","",name).upper()
            if value==session["user"]:
                flash(f"Welcome,{name}!You've registered successfully","success")
                return redirect(url_for("success"))
            else:
                flash(f"Another person,Please fill it again","error")
                return redirect(url_for("success"))
        
    
    return render_template("registration.html",form=RegForm)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("loginform"))

if __name__=="__main__":
    app.run(debug=True)



