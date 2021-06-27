def add_hospitals(name,email,username,password,address):
    query = """INSERT INTO Hospitals(name, email, username, password, address)
	VALUES('{}', '{}', '{}', '{}', '{}');"""
    return query.format(name, email, username, password, address)

#******************************************************

def add_bloodbank(name,email,username,password,address):
    query = """INSERT INTO BloodBanks(name, email, username, password, address)
	VALUES('{}', '{}', '{}', '{}', '{}');"""
    return query.format(name, email, username, password, address)

#******************************************************

def get_hospitals():
    return """SELECT * FROM Hospitals;"""

#******************************************************

def get_bloodbanks():
    return """SELECT * FROM BloodBanks;"""

#******************************************************

  
