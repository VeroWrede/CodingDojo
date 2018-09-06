from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'donottell'

@app.route("/")
def index():
    if "num" not in session:
        session["num"] = 1
    
    return render_template("index.html", num=session["num"])

@app.route("/add", methods=["POST"])
def add():
    session["num"] += 2
    return redirect("/")

@app.route("/clear", methods=["POST"])
def clear():
    session.clear()
    return redirect("/")

app.run(debug=True)