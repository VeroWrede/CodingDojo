from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
	query = 'SELECT * FROM friends'
	friends = mysql.query_db(query)
	print (friends)
   	return render_template('index.html', all_friends = friends)
@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends (first_name, occupation, created_at, updated-at) VALUES (:first_name, :last_name, :occupation, :now(), :now())"
	data = {
	'first_name': request.form['first_name'],
	'last_name': request.form['last_name'],
	'occupation': request.form['occupation'],
	}
	mysql.query_db(query,data)
	return redirect('/')
@app.route('/friends/<friend_id>')
def show(friend_id):
	query = 'SELECT * FROM friend WHERE id = :specific_id'
	data = {'specific_id': friend_id}
	friends = mysql.query_db(query, data)
	return render_template('index.html', one_friend = friends[0])
app.run(debug=True)