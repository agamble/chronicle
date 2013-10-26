import sqlite3
DATABASE = 'our.db'

class DatabaseManager(object):
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE)
        self.cur = self.conn.cursor()

    # this function takes a string as the command, and a tuple of the args in the position they need to be stored in the db
    # returns the row of the last command
    def write_to_db(self, command, args):
        self.cur.execute(command, args)

        self.conn.commit()

        return self.cur.lastrowid

    def query(self, command, args):
        if args:
            self.cur.execute(command, args)
        else:
            self.cur.execute(command)
        results = self.cur.fetchall()
        return results

    def __del__(self):
        self.conn.close()