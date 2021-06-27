def add_hospitals(name,email,username,password,address, phone, info):
    query = """INSERT INTO Hospitals(name, email, username, password, address, phone, info)
	VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
    return query.format(name, email, username, password, address, phone, info)

#******************************************************

def add_bloodbank(name,email,username,password,address, phone, info):
    query = """INSERT INTO BloodBanks(name, email, username, password, address, phone, info)
	VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
    return query.format(name, email, username, password, address, phone, info)

#******************************************************

def get_hospitals():
    return """SELECT name, email, address, phone, info FROM Hospitals"""

#******************************************************

def get_bloodbanks():
    return """SELECT name, email, address, phone, info FROM BloodBanks"""

#******************************************************

  
