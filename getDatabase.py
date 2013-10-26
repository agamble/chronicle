def getEventsForGroup(groupID, d):

	return d.query("SELECT * FROM events WHERE groupid=?",[groupID])


