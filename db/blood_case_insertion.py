
def insert_blood_case(id, blood_bank_id, case_type, blood_class, storing_date, expiration_date):
    query = "INSERT INTO BloodCases(id, bloodBankId, type, bloodClass, storingDate, expirationDate) VALUES ({}, {}, '{}', '{}', '{}', '{}')"
    return query.format(id, blood_bank_id, case_type, blood_class, storing_date, expiration_date)

