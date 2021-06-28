def Add_User_Donations( id, userid, bloodbankid , status, donationdate, bags, createdat):
 query = """INSERT INTO public.donations(id, userid, bloodbankid, status, donationdate, bags, createdat) VALUES ({},{},{},{},{},{},{})"""
 return query.format(id, userid, bloodbankid, status, donationdate, bags, createdat)