from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('homepage.html')

app.run(debug=True)