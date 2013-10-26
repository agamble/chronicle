from flask import Flask, request
from database import DatabaseManager
import psycopg2
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
	d = DatabaseManager()
	values = d.query("SELECT * FROM users", None)
	if values:
		return 'it works'

@app.route('/<university>/')
def another():
	return

if __name__ == '__main__':
	app.run(debug=True)