import bcrypt

def hash_password(password):
	hash = password.encode('utf-8')
	return bcrypt.hashpw(hash, bcrypt.gensalt())

def verify_password(password, hashed_password):
	hash = password.encode('utf-8')
	hash2 = hashed_password.encode('utf-8')
	if bcrypt.hashpw(hash, hash2) == hash2:
		return True
	else:
		return False

def get_user_data(request):
	user_dict = {}
	request.cookies.get('name')

def validateEmail(email):
	if email.find("@") == -1:
		return False
	else:
		return True

def verifyLoggedIn(request):
	if request.cookies.get('name'):
		return request.cookies.get('name')
	else:
		return False


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

def loginValid(email, password, d):


	user = d.query("SELECT * FROM users WHERE email=?", [email])
	print user

	if not user:
		return False

	hashed_password = user[0][3]

	if verify_password(password, hashed_password):

		return user[0][2]
	else:
		return False

