

def delete_blood_case(id):
    query = """ update BloodCases set isDeleted = true where BloodCases.id= '{}' """

    return query.format(id)

def get_donation_request(id):
    query = """ select Orders.id , Orders.bloodBankId , Orders.hospitalId , Orders.amount , Orders.bloodClass
        from Orders where bloodBankId = '{}' and Orders.status = 'Pending' """
    return query.format(id)