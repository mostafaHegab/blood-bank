def add_user(name, email, password, gender, birthdate, bloodClass):
    query = """INSERT INTO Users(name, email, password, gender, birthdate, bloodClass)
	VALUES ('{}', '{}', '{}', '{}','{}', '{}')"""
    return query.format(name, email, password, gender, birthdate, bloodClass)


def get_user_by_email(email):
    query = """select id,name, password FROM Users WHERE email = '{}'"""
    return query.format(email)
