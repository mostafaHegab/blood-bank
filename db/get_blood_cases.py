def get_blood_cases(bank_id , blood_class):
    query = """SELECT BloodCases.id from BloodCases where bloodBankId = {} and bloodClass = '{}' order by expirationDate asc"""
    return query.format(bank_id , blood_class)