def get_donation_request(id):
    query = """SELECT Users.id, name, birthDate, email, gender, weight, hasDiseases, lastTreatmentDate, bloodClass, lastDonationDate FROM Users INNER JOIN Donations ON Donations.userId = Users.id WHERE Donations.bloodBankId = {} AND Donations.status = 'Pending'"""
    return query.format(id)
