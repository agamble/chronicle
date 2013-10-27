
def getUserID(email, d):
    return d.query('SELECT userid FROM users WHERE email = ?', email)

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
    return d.write_to_db('INSERT INTO files (eventid, userid, added_date, file_content, description, file_location) VALUES (?, ?, ?, ?, ?, ?)', eventID, userID, addedDate, fileContent, description, fileLocation)

def setComment(userID, fileID, date, time, coOrdX, coOrdY, ranking, contents, d):
    return d.write_to_db('INSERT INTO comments (userid, fileid, date, time, coordx, xoordy, ranking, contents) VALUES (?, ?, ?, ?, ?, ?, ?', userID, fileID, date, time, coOrdX, coOrdY, ranking, contents)


