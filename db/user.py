def add_user(name, email, password, gender, age):
    query = """INSERT INTO Donners(name, email, password, gender, age)
	VALUES ('{}', '{}', '{}', '{}','{}')"""
    return query.format(name, email, password, gender, age)



def get_user_by_email(email):
    query = """select id,name,password FROM Users WHERE email = '{}'"""
    return query