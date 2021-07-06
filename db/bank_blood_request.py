def add_new_blood_request(bloodBankId, hospitalId, amount, bloodClass, bloodType, date):
    query = """INSERT INTO Orders(bloodBankId, hospitalId, amount, bloodClass, type, date) VALUES({}, {}, {}, '{}', '{}', '{}')"""
    return query.format(bloodBankId, hospitalId, amount, bloodClass, bloodType, date)
