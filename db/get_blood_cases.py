def get_blood_cases(bank_id, blood_class, type):
    query = """SELECT BloodCases.id from BloodCases where bloodBankId = {} and bloodClass = '{}' and BloodCases.type ='{}' and not isdeleted order by expirationDate asc"""
    return query.format(bank_id, blood_class, type)
