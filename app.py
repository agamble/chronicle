from flask import Flask, request
from database import DatabaseManager
import register


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

@app.route('/<university>/register', methods=['GET', 'POST'])
def uni_register():
	d = DatabaseManager()

	if request.method == "POST":
		username, password = request.form['username'], request.form['password']
		register(email, password, password, d)
	if request.method == "GET":
		return render_template('register.html')

if __name__ == '__main__':
	app.run(debug=True)