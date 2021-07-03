def get_user_donations(id):
    query = """SELECT Donations.id AS donationId, status, BloodBanks.name AS bankName,CONCAT(Governorates.name,' , ',Cities.name,' , ',BloodBanks.street) AS Address,donationDate,bags FROM Donations INNER JOIN BloodBanks ON Donations.bloodBankId = BloodBanks.id AND Donations.status = 'pending' INNER JOIN Cities ON BloodBanks.cityId = Cities.id INNER JOIN Governorates ON Cities.governorateId = Governorates.id INNER JOIN Users ON Users.id= {}"""
    return query.format(id)

# ------------------------------------------------------------------------------------------------------------------------


def add_user_donations(userId, bloodBankId, createdAt):
    query = """INSERT INTO public.donations(userId, bloodBankId,  createdAt) VALUES ({},{},'{}')"""
    return query.format(userId, bloodBankId, createdAt)

# -------------------------------------------------------------------------------------------------------------------------


def update_user(weight, hasDiseases, lastTreatmentDate, userId, lastDonationDate):
    query = """UPDATE public.users SET weight={}, hasDiseases={}, lastTreatmentDate='{}', lastDonationDate='{}' WHERE users.id = {}"""
    return query.format(weight, hasDiseases, lastTreatmentDate, lastDonationDate, userId)


def get_bloodbanks():
    return """SELECT bloodbanks.id, bloodbanks.name from bloodbanks"""
