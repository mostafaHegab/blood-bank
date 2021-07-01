def add_user(name, email, password, gender, birthdate, bloodClass):
    query = """INSERT INTO Users(name, email, password, gender, birthdate, bloodClass)
	VALUES ('{}', '{}', '{}', '{}','{}', '{}')"""
    return query.format(name, email, password, gender, birthdate, bloodClass)


def get_user_by_email(email):
    query = """select id,name, password FROM Users WHERE email = '{}'"""
    return query.format(email)


def delete_blood_case(id):
    query = """ delete from BloodCases where BloodCases.id= '{}',
    update BloodCases set isDeleted = true where BloodCases.id= '{}' """

    return query.format()

def get_donation_request(id):
    query = """ select Orders.id , Orders.bloodBankId , Orders.hospitalId , Orders.amount , Orders.bloodClass
        from Orders where bloodBankId = '{}' and Orders.status = 'pending' """
    return query.format()