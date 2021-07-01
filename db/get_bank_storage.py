def get_bank_Storage():
    return """SELECT id,type,bloodClass,storingDate,expirationDate FROM BloodCases WHERE BloodCases.orderId IS null AND isDeleted = 'False' ORDER BY expirationDate DESC"""