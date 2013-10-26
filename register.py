import database

def hash_password(password):
	return bcrypt.hashpw(password, bcrypt.gensalt())

def register(email, name, password, university, d):

	hashed_password = hash_password()

	user_tuple = (email, name, hashed_password)

	test_email = d.query("SELECT * FROM users WHERE email = ?", email)

	if test_email:
		return False

	user_id = d.write_to_database("INSERT INTO users (email, name, pw) VALUES (?,?,?)", user_tuple)

	if user_id:
		return user_id
	else:
		return False