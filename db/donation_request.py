def get_donation_request(id):
    query = """SELECT donations.id, name, birthDate, email, gender, weight, hasDiseases, lastTreatmentDate, bloodClass, bloodtype, lastDonationDate FROM Users INNER JOIN Donations ON Donations.userId  = Users.id WHERE donations.bloodBankId = {} AND Donations.status = 'pending'"""
    return query.format(id)


def get_donation_details(id):
    query = """SELECT donations.id AS donationid, users.id AS userid, name, birthDate, email, gender, weight, hasDiseases, lastTreatmentDate, bloodClass, bloodtype, lastDonationDate FROM Users INNER JOIN Donations ON Donations.userId  = Users.id WHERE donations.id = {}"""
    return query.format(id)

def accept_donation_request(id, donationDate):
    query = """UPDATE donations SET status = 'accepted', donationdate = '{}' WHERE id = {}"""
    return query.format(donationDate, id)
