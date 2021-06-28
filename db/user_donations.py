def get_user_donations(id):
 query = """SELECT Donations.id AS DonationId,BloodBanks.name AS BankName,CONCAT(Governorates.name,' , ',Cities.name,' , ',BloodBanks.street) AS Address,donationDate,bags FROM Donations INNER JOIN BloodBanks ON Donations.bloodBankId = BloodBanks.id INNER JOIN Cities ON BloodBanks.cityId = Cities.id INNER JOIN Governorates ON Cities.governorateId = Governorates.id INNER JOIN Users ON Users.id= {}"""
 return query.format(id)

#------------------------------------------------------------------------------------------------------------------------

def add_user_donations(userid, bloodbankid , donationdate, createdat):
 query = """INSERT INTO public.donations(userid, bloodbankid, status,donationdate, createdat) VALUES ({},{},benging,{},{})"""
 return query.format(userid, bloodbankid, donationdate, createdat)

#-------------------------------------------------------------------------------------------------------------------------
def update_user(weight,hasdiseases,lasttreatmentdate,userid):
 query = """UPDATE public.users SET weight={}, hasdiseases={}, lasttreatmentdate={} WHERE users.id = {}"""
 return query.format(weight,hasdiseases,lasttreatmentdate,userid)
