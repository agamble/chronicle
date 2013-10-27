def getEventsForGroup(groupID, d):
	return d.query("SELECT * FROM events WHERE groupid=?",[groupID])

def getNotesForEvent(EventID, d):
	return d.query("SELECT * FROM files WHERE groupid=?", [EventID])

def getEventURLs(EventID, d):
	return d.query("SELECT * FROM globalFiles WHERE eventid=?", [EventID])

def getFiles(eventid, d):
	query = d.query("SELECT * FROM files WHERE eventid=?", [EventID])
	query_array = []
	for index, element in enumerate(query):
		query.append({})
		query_array[index][userid] = element[3]
		query_array[index][file_content] = element[4]
		query_array[index][description] = element[5]
	return query_array

def getFileList(eventid, d):
	return d.query("SELECT * FROM files where eventid=?", [eventid])
