from flask import Flask, request, render_template
from database import DatabaseManager
from usermanagement import *
import calendar
from datetime import date

cal = calendar.HTMLCalendar(0)


app = Flask(__name__)

@app.route('/')
def index():
	d = DatabaseManager()
	this_month_cal = cal.formatmonth(2013, 10)
	values = d.query("SELECT * FROM users", None)
	if values:

		return render_template('index.html', cal=this_month_cal)


@app.route('/<university>/<short_group>/')
def group_page(university=None, short_group=None):
	return university

@app.route('/login', methods=['GET', 'POST'])
def login():
	d = DatabaseManager()

	if request.method == "POST":
		email, password = request.form['email'], request.form['password']
		username = loginValid(email, password, d)
		print email, password
		if username:
			resp.set_coookie('name', username)
			return render_template('index.html')
		else:
			return render_template('login.html')

	if request.method == "GET":

		return render_template('login.html')

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

@app.route('/<university>/<short_group>/<int:event_id>/<int:note_id>')
def show_note(university=None, short_group=None, event_id=0, note_id=0):

	d = DatabaseManager()

@app.route('/<university>/<short_group>')
def show_events(university=None, short_group=None):

	d = DatabaseManager()



if __name__ == '__main__':
	app.run(debug=True)

