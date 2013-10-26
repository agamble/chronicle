import database
import bcrypt

def hash_password(password):
	hash = password.encode('utf-8')
	return bcrypt.hashpw(hash, bcrypt.gensalt())

def validateEmail(email):
	if email.find("@") == -1:
		return False
	else:
		return True

def register(email, name, password, university, d):
	hashed_password = hash_password(password)
	user_tuple = (email, name, hashed_password)

	test_user = d.query("SELECT * FROM users WHERE email=?", [email])
	print test_user
	if test_user:
		return False
	print "got this far"

	if not validateEmail(email):
		return False


	user_id = d.write_to_db("INSERT INTO users (email, name, pw) VALUES (?,?,?)", user_tuple)
	if user_id:
		print "The user " + email + " was successfully added!"
		return user_id
	else:
		return False

def login(email, password, d):

	hashed_password = hash_password(password)



