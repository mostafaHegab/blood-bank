def blood_requests_for_hospital(hospitalId):
    query = """SELECT Orders.id, BloodBanks.name, Orders.date, BloodBanks.email, concat(BloodBanks.street, ',', Cities.name, ',', Governorates.name) , Orders.amount, Orders.type, Orders.bloodClass,Orders.status FROM BloodBanks INNER JOIN Cities ON BloodBanks.cityId = Cities.id INNER JOIN Governorates ON Cities.governorateId = Governorates.id INNER JOIN Orders ON BloodBanks.id = Orders.bloodBankId WHERE Orders.hospitalId = {} ORDER BY Orders.date DESC"""
    return query.format(hospitalId)
