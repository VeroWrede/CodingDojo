from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welocme_page():
	return render_template("index.html")

@app.route('/ninjas')
def ninjas():
	return render_template("ninjas.html")

@app.route('/dojo')
def new_ninja_form():
	return render_template("")

@app.route('/dojo/new', methods=['POST'])
def create_new_user():
	name = request.form['name']
	gender = request.form['gender']
	return redirect('/dojo')

app.run(debug=True)