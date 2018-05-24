# create directory the create a python file and open in text editor

from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello():
	return 'hello'

app.run(debug=True)

# go to cmd and type 'python fileName.py'
# to see output go to localhost:5000