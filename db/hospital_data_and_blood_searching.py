def get_hospital_data_by_email(email):
    query = """SELECT id, email, password FROM  Hospitals WHERE email = '{}'"""
    return query.format(email)


# -----------------------------------------------------------------------


def search_for_blood(blood_type, blood_class, hospital_id):
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
	FROM Hospitals 
	INNER JOIN BloodBanks
	ON 
	BloodBanks.cityId = Hospitals.cityId 
	INNER JOIN 
	Cities
	ON
	Cities.id = BloodBanks.cityID
	INNER JOIN
	Governorates 
	ON Governorates.id = Cities.id 
	INNER JOIN
	BloodCases
	ON
	BloodCases.bloodBankId = BloodBanks.id
	WHERE Bloodcases.isDeleted = FALSE
	AND Bloodcases.orderId IS NULL 
	AND BloodCases.type = '{}'
	AND BloodCases.bloodClass = '{}'
	AND Hospitals.id = {}) As BankInfo"""
    return query.format(blood_type, blood_class, hospital_id)
