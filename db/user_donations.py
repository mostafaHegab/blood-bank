def Get_User_Donations(id):
 query = """SELECT Donations.id AS DonationId,BloodBanks.name AS BankName,CONCAT(Governorates.name,' , ',Cities.name,' , ',BloodBanks.street) AS Address,donationDate,bags FROM Donations INNER JOIN BloodBanks ON Donations.bloodBankId = BloodBanks.id INNER JOIN Cities ON BloodBanks.cityId = Cities.id INNER JOIN Governorates ON Cities.governorateId = Governorates.id INNER JOIN Users ON Users.id= {}"""
 return query.format(id)
