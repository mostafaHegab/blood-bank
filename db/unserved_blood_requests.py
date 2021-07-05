def get_unserved_requests(bankId):
 query = """SELECT Orders.id,Hospitals.name ,CONCAT(Governorates.name,' , ',Cities.name,' , ',Hospitals.street) AS Address,amount ,date FROM Orders INNER JOIN Hospitals ON Orders.hospitalId = Hospitals.id INNER JOIN Cities ON Hospitals.cityId = Cities.id INNER JOIN Governorates ON Cities.governorateId = Governorates.id WHERE orders.bloodBankId = {} AND Orders.status = 'pending'"""
 return query.format(bankId)