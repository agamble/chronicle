import database

def hash_password(password):
	return bcrypt.hashpw(password, bcrypt.gensalt())

def register(email, name, password, university, d):

	hashed_password = hash_password(password)

	user_tuple = (email, name, hashed_password)

	test_user = d.query("SELECT * FROM users WHERE email = ?", email)

	if test_user:
		return False

	user_id = d.write_to_database("INSERT INTO users (email, name, pw) VALUES (?,?,?)", user_tuple)

	if user_id:
		return user_id
	else:
		return False

def login(email, password, d):

	hashed_password = hash_password(password)

	


