def get_bloodbanks_by_email(email):
    query = """SELECT BloodBanks.id, BloodBanks.email, BloodBanks.password FROM BloodBanks WHERE BloodBanks.email = '{}'"""" 
    return query.format(email)

#******************************************************

def get_dobations_history_by_bank(id):
    query = """SELECT Users.id, name, birthDate, email, gender, weight, hasDiseases, lastTreatmentDate, bloodClass, lastDonationDate FROM Users INNER JOIN Donations ON Donations.userId = Users.id WHERE Donations.id = {} AND Donations.status != 'Pending'"""
    return query.format(id)
