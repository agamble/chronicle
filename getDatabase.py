def getEventsForGroup(groupID, d):
	return d.query("SELECT * FROM events WHERE groupid=?",[groupID])

def getNotesForEvent(EventID, d):
	return d.query("SELECT * FROM files WHERE groupid=?", [EventID])

def getEventURLs(EventID, d):
	return d.query("SELECT * FROM globalFiles WHERE eventid=?", [EventID])

def getUser(name, d):
	return d.query("SELECT * FROM users WHERE name=?", [name])

def getFiles(eventid, d):
	query = d.query("SELECT * FROM files WHERE eventid=?", [eventid])
	query_array = []
	for index, element in enumerate(query):
		query.append({})
		query_array[index][userid] = element[2]
		query_array[index][date] = element[3]
		query_array[index][file_content] = element[4]
		query_array[index][description] = element[5]
	return query_array

def getUserID(name, d):
	return d.query("SELECT * FROM users WHERE name=?", [name])[0][0]

def getUserGroups(userid, d):
	all_my_groups =	d.query("SELECT * FROM enrolment WHERE userid LIKE ?", [userid])
	groups_array = []
	print all_my_groups
	for enrolment in all_my_groups:
		groups_array.append(enrolment[1])
	return groups_array

def allUserEventsforCalendar(groups_array, d):
	event_array = []
	for group in groups_array:
		my_events = d.query("SELECT * FROM events WHERE groupid=?", [group])
		for event in my_events:
			event_array.append(event)
	print len(event_array)
	for event in event_array:
		date = event[2]
		name = event[4]

def getFileList(eventid, d):
	return d.query("SELECT * FROM files where eventid=?", [eventid])
