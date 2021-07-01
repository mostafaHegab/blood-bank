def get_bank_Storage(id):
    query = """SELECT id,type,bloodClass,storingDate,expirationDate FROM BloodCases WHERE BloodCases.orderId IS null AND isDeleted = 'False' AND BloodCases.bloodBankId = {} ORDER BY expirationDate ASC"""
    return query.format(id)