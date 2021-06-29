def get_user_donations(id):
 query = """SELECT Donations.id AS donationId,BloodBanks.name AS bankName,CONCAT(Governorates.name,' , ',Cities.name,' , ',BloodBanks.street) AS Address,donationDate,bags FROM Donations INNER JOIN BloodBanks ON Donations.bloodBankId = BloodBanks.id INNER JOIN Cities ON BloodBanks.cityId = Cities.id INNER JOIN Governorates ON Cities.governorateId = Governorates.id INNER JOIN Users ON Users.id= {}"""
 return query.format(id)

#------------------------------------------------------------------------------------------------------------------------

def add_user_donations(userId, bloodBankId , donationDate, createdAt):
 query = """INSERT INTO public.donations(userId, bloodBankId, status,donationDate, createdAt) VALUES ({},{},'bending','{}','{}')"""
 return query.format(userId, bloodBankId, donationDate, createdAt)

#-------------------------------------------------------------------------------------------------------------------------
def update_user(weight,hasDiseases,lastTreatmentDate,userId):
 query = """UPDATE public.users SET weight={}, hasDiseases={}, lastTreatmentDate='{}' WHERE users.id = {}"""
 return query.format(weight,hasDiseases,lastTreatmentDate,userId)
