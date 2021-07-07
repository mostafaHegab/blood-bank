def add_hospitals(name,email,password, phone, street, cityId, info, createdAt):
    query = """INSERT INTO Hospitals(name,email,password, phone, street, cityId, info, createdAt)
	VALUES('{}', '{}', '{}', '{}', '{}', {}, '{}', '{}')"""
    return query.format(name,email,password, phone, street, cityId, info, createdAt)

#******************************************************

def add_bloodbank(name,email,password,phone, street, cityId, info,createdAt):
    query = """INSERT INTO BloodBanks(name,email,password,phone, street, cityId, info,createdAt)
	VALUES('{}', '{}', '{}', '{}', '{}', {}, '{}', '{}')"""
    return query.format(name,email,password,phone, street, cityId, info,createdAt)

#******************************************************

def get_hospitals():
    return """SELECT hospitals.id, hospitals.name, email, concat(street, ',', Cities.name, ',', Governorates.name), phone, info, createdAt FROM Hospitals INNER JOIN Cities ON Hospitals.cityId = Cities.id INNER JOIN Governorates ON Cities.governorateId = Governorates.id ORDER BY createdAt DESC"""

#******************************************************

def get_bloodbanks():
    return """SELECT bloodbanks.id, bloodbanks.name, email, concat(street, ',', Cities.name, ',', Governorates.name), phone, info, createdAt FROM BloodBanks INNER JOIN Cities ON BloodBanks.cityId = Cities.id INNER JOIN Governorates ON Cities.governorateId = Governorates.id ORDER BY createdAt DESC"""

#******************************************************

  
