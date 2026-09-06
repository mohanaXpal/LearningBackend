from flask import Flask,render_template,request,session,redirect,url_for,Response
students={
    "MOHANA" :{
        "pass":"1h567*6",
        "year":"1st",
        "department":"CSE",
        "subjects":["physics","math-1","cs"],
        "cgpa":9.045
    },
    "MRITTIKA" :{
            "pass":"hello#7895",
            "year":"1st",
            "department":"IT",
            "subjects":["chemistry","math-2","dsa","dla"],
            "cgpa":9.0
        },
    "SUVAM" :{
            "pass":"hklti59",
            "year":"4th",
            "department":"CSE",
            "subjects":["chemistry","math-2","dsa","dla"],
            "cgpa":8.99
        },
    "RUPAM" :{
            "pass":"rup@kjf45",
            "year":"4th",
            "department":"IT",
            "subjects":["physics","math-2","dsa","dla"],
            "cgpa":8.66
        }
}
app=Flask(__name__)
app.secret_key="iuy4pi5kg"
@app.route("/")
def login():
    return render_template("login.html")


@app.route("/submit" ,methods=["POST"])
def submit():
    username=request.form.get("username").upper()
    password=request.form.get("password")
    if username in students and password==students[username]["pass"]:
      
        session["user"]=username
        session["pass"]=password
        return redirect(url_for("profile"))
    else:
        return Response("Invalid Password ,try again later" ,mimetype="text/plain")


@app.route("/profile")
def profile():
    if "user" in session and "pass" in session :
        username=session["user"]
        student=students[username]
        return render_template("profile.html",name=session["user"],year=student["year"],department=student["department"],sub=student["subjects"],cgpa=student["cgpa"])


@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("login"))


if __name__== '__main__':
    app.run(debug=True)