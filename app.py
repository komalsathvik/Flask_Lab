from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/handle_login",methods=["GET","POST"])
def handle_login():
    if request.method=="GET":
        print(request.username)
        return "<h1>entered into GET METHOD"
    else:
        return f"<h1> Welcome {request.form["username"]} </h1>"
@app.route("/content")
def content():
    value=123
    arr=[1,2,3,4,5]
    return render_template("content.html",arr=arr,value=value)
app.run(debug=True)