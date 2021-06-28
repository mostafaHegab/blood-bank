
def get_bank_data_by_email(email):
    query = """SELECT
	BankInfo.Id,  
	BankInfo.Name,
	BankInfo.Email,
	CONCAT(
	BankInfo.GovernorateName,
	', ',
	BankInfo.CityName,
	', ',
	BankInfo.Street,
	' St.') AS Address,	
	BankInfo.Phone,
	BankInfo.Info,
	BankInfo.CreatedAt
 	FROM 
	(SELECT
	BloodBanks.id AS Id,
	BloodBanks.name AS Name,
	BloodBanks.email AS Email,
	BloodBanks.phone AS Phone,
	BloodBanks.info AS Info,
	BloodBanks.createdAt AS CreatedAt, 
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
	WHERE Bloodbanks.cityId = Cities.id) As BankInfo
	WHERE BankInfo.Email = {}"""

    return query.format(email)

#----------------------------------------------------------

def get_bank_storage_by_bank_id(bank_id):
    query = """SELECT
	Storage.bankId,
	Storage.caseId,
	Storage.type,
	Storage.bloodClass,
	Storage.expirationDate
	FROM
	(SELECT
	BloodBanks.id As bankId,
	BloodCases.id AS caseId,
	BloodCases.type,
	BloodCases.bloodClass,
	BloodCases.expirationDate
	FROM
	BloodCases
	INNER JOIN
	BloodBanks
	ON
	BloodCases.bloodBankId = BloodBanks.id) AS Storage
	WHERE 
	Storage.bankId = {}
	ORDER BY 
	Storage.expirationDate DESC"""

    return query.format(bank_id)

#----------------------------------------------------------

def delete_blood_case_by_its_id(case_id):
    query = "DELETE FROM BloodCases WHERE BloodCases.id = {}"
    return query.format(case_id)