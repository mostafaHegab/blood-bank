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

def search_for_blood(blood_type, blood_class):
    query = """SELECT DISTINCT
	BankInfo.id,  
	BankInfo.name,
	CONCAT(
	BankInfo.governorateName,
	', ',
	BankInfo.cityName,
	', ',
	BankInfo.street,
	' St.') AS address
 	FROM 
	(SELECT
	BloodBanks.id AS id,
	BloodBanks.name AS name,
	Governorates.name AS governorateName,
	Cities.name AS cityName,
 	BloodBanks.street AS street
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
	BloodCases.type = 'type1'
	AND
	BloodCases.bloodClass = 'A+')As BankInfo"""
    return query.format(blood_type, blood_class)
