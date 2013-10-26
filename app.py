from flask import Flask, request, render_template
from database import DatabaseManager
from usermanagement import *


app = Flask(__name__)

@app.route('/')
def index():
	d = DatabaseManager()
	values = d.query("SELECT * FROM users", None)
	if values:
		return 'it works'

@app.route('/<university>/<short_group>/')
def group_page(university=None, short_group=None):
	return university

@app.route('/login')
def login():
	return

@app.route('/<university>/register', methods=['GET', 'POST'])
def uni_register(university=None):

	d = DatabaseManager()

	if request.method == "POST":
		email, password, name = request.form['email'], request.form['password'], request.form['name']
		
		row_id = register(email, name, password, university, d)
		if row_id:
			return render_template('register.html')

	if request.method == "GET":
		return render_template('register.html')

if __name__ == '__main__':
	app.run(debug=True)