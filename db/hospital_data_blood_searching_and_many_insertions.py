def get_hospital_data_by_email(email):
    query = """SELECT
	id,  
	email,	
	password
 	FROM 
	Hospitals
	WHERE email = {}"""
    return query.format(email)


# -----------------------------------------------------------------------

def insert_blood_case(blood_bank_id, case_type, blood_class, storing_date, expiration_date):
    query = """INSERT INTO BloodCases(bloodBankId, type, bloodClass, storingDate, expirationDate)
	VALUES({}, {}, {}, {}, {})"""

    return query.format(blood_bank_id, case_type, blood_class, storing_date, expiration_date)

# ------------------------------------------------------------------------

def search_for_blood(blood_type, blood_class):
    query = """SELECT DISTINCT
	BankInfo.Id,  
	BankInfo.Name,
	CONCAT(
	BankInfo.GovernorateName,
	', ',
	BankInfo.CityName,
	', ',
	BankInfo.Street,
	' St.') AS Address
 	FROM 
	(SELECT
	BloodBanks.id AS Id,
	BloodBanks.name AS Name,
	Governorates.name AS GovernorateName,
	Cities.name AS CityName,
 	BloodBanks.street AS Street
	FROM Cities 
	INNER JOIN 
	BloodBanks 
	ON 
	BloodBanks.cityId = Cities.id 
	INNER JOIN 
	Governorates 
	ON Governorates.id = Cities.id 
	INNER JOIN
	BloodCases
	ON
	BloodCases.bloodBankId = BloodBanks.id
	WHERE 
	BloodBanks.cityId = Cities.id
	AND
	BloodBanks.id = BloodCases.bloodBankId
	AND 
	BloodCases.type = {}
	AND
	BloodCases.bloodClass = {})As BankInfo"""

    return query.format(blood_type, blood_class)
