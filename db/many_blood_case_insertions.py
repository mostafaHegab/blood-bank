def insert_blood_cases(blood_bank_id, case_type, blood_class, storing_date, expiration_date, count):
    formatted_rows = ''
    query = "INSERT INTO BloodCases(bloodBankId, type, bloodClass, storingDate, expirationDate) VALUES "
    rows = "({}, '{}', '{}', '{}', '{}')"

    for i in range(count):
        formatted_rows += rows.format(blood_bank_id, case_type, blood_class, storing_date, expiration_date) + ','

    return query + formatted_rows.rstrip(formatted_rows[-1])