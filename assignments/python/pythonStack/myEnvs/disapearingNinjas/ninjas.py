from flask import Flask, render_template, redirect
app = Flask(__name__)
app.secret_key = "pssssssst"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninja")
def ninjas():
    return render_template("found.html")

@app.route("/ninja/<color>")
def word(color):
    if color == "blue":
        return render_template("blue.html")
    elif color == "red":
        return render_template("red.html")
    elif color == "green":
        return render_template("green.html")
    else:
        return render_template("april.html")

app.run(debug=True)