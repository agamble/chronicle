from flask import Flask, request, render_template, make_response, redirect
from database import DatabaseManager
from usermanagement import *
import calendar
from datetime import date
import os
from requestCalendar import importICStoDatabase
from getDatabase import *
cal = calendar.HTMLCalendar(0)
universities = [
				'ucl',
				'berkeley'
				
				]

app = Flask(__name__)




def getUserName(ID, d):
    return d.query('SELECT name FROM users WHERE name = ?', name)

def getUser(userID, d):
    return d.query('SELECT * FROM users WHERE userID = ?', userID)

def getUserEvents(userID, d):
    return d.query('SELECT * FROM events, enrolment WHERE events.groupid = enrolment.groupid AND enrolment.userid = ?', userID)

def getEvent(eventID, d):
    return d.query('SELECT * FROM events WHERE eventid = ?', eventID)

def getEventFiles(eventID, d):
    return d.query('SELECT * FROM files WHERE eventid = ?', eventID)

def getFile(fileID, d):
    return d.query('SELECT * FROM files WHERE fileid = ?', fileID)

def getComment(commentID, d):
    return d.query('SELECT * FROM comment WHERE commentid =?', commentID)

def setUser(userID, email, name, pw, uniShort, d):
    return d.write_to_db('INSERT users (email, name, PW, uniShort) VALUES (?,?,?,?)', email, name, pw, uniShort)

def setEvent(groupID, date, summary, d):
    return d.write_to_db('INSERT INTO events (groupIid, date, summary) VALUES (?,?,?)',  groupID, date, summary)

def setEnrolment(groupID, userID, d):
    return d.write_to_db('INSERT INTO enrolment (groupid, userid) VALUES (?,?)', groupID, userID)

##Add the whole name (including the file extension) in the description field
def setFile(eventID, userID, addedDate, fileContent, description, fileLocation, d):
	if (fileLocation is None) and (description is None):
	    return d.write_to_db('INSERT INTO files (eventid, userid, added_date, file_content) VALUES (?, ?, ?, ?)', eventID, userID, addedDate, fileContent)

def setComment(userID, fileID, date, time, coOrdX, coOrdY, ranking, contents, d):
    return d.write_to_db('INSERT INTO comments (userid, fileid, date, time, coordx, xoordy, ranking, contents) VALUES (?, ?, ?, ?, ?, ?, ?', userID, fileID, date, time, coOrdX, coOrdY, ranking, contents)




@app.route('/')
def index():
	name = verifyLoggedIn(request)
	d = DatabaseManager()
	this_month_cal = cal.formatmonth(2013, 10)
	if name:
		print name
		groups_array = getUserGroups(name, d)
		print groups_array
		events = allUserEventsforCalendar(groups_array, d)
		return render_template('index.html', cal=this_month_cal, name=name, events=events)
	else:
		return render_template('index.html')


@app.route('/<university>/<short_group>/')
def group_page(university=None, short_group=None):
	return university

@app.route('/login', methods=['GET', 'POST'])
def login():
	d = DatabaseManager()
	name = verifyLoggedIn(request)
	if request.method == "POST":
		email, password = request.form['email'], request.form['password']
		username = loginValid(email, password, d)
		print email, password
		if username:
			resp = make_response(render_template('index.html', name=username, loggedIn=True))
			resp.set_cookie('name', username)
			return resp
		else:
			return render_template('login.html', name=name)

	if request.method == "GET":
		return render_template('login.html')

@app.route('/<university>/<int:groupid>/<int:eventid>/')
def event_page(university=None, groupid=0, eventid=0):
	d = DatabaseManager()
	name = verifyLoggedIn(request)


	query = d.query("SELECT * FROM files where eventid=?", [eventid])

	group = d.query("SELECT * FROM groups where groupid=?", [groupid])

	short_group_name = group[0][1]

	files = getFiles(eventid, d)

	if query:
		return render_template('event.html', name=name, group_name=short_group_name, files=files)
	else:
		abort(404)

@app.route('/<university>/<int:short_group>/<int:event_id>/upload', methods=['GET', 'POST'])
def upload_note(university=None, short_group=None, event_id=0):
	d = DatabaseManager()
	name = verifyLoggedIn(request)

	if request.method == "POST":
		title, content = request.form['title'], request.form['note_entry']

		setFile(short_group, eventid, datetime.date, content, None, None, d)
	if request.method == "GET":
		return render_template('upload_note.html', name=name)

@app.route('/<university>/register', methods=['GET', 'POST'])
def uni_register(university=None):

	d = DatabaseManager()
	name = verifyLoggedIn(request)

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

	files_list = getFiles(event_id, d)

	return render_template('event.html', files_list=files_list)


@app.route('/_ics_import')
def grab_calendar_data():
	d = DatabaseManager()
	name = verifyLoggedIn(request)

	user = getUser(name, d)


	importICStoDatabase("http://www.ucl.ac.uk/timetable/ics/spxipmlh28sgtpd", d, user[0])

	return "IT WORKED!"



if __name__ == '__main__':
	app.run(debug=True)

