Def GetUserDonations(id):
	query = """
	SELECT 
		Donations.id AS Donation_Id,
		BloodBanks.name AS Bank_NAme,
		BloodBanks.address AS Bank_Address,
		donationDate,
		count AS Bags
	FROM Donations 
	INNER JOIN BloodBanks 
		ON Donations.bloodBankId = BloodBanks.id
	INNER JOIN Donners
		ON Donners.id={}"""
    return query.format(id)