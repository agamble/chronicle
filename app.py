from flask import Flask, request
import database, login
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
	if userIsLoggedIn():
		return ' You are logged in!'

@app.route('/<university>/')
def 

if __name__ == '__main__':
    app.run()