def add_new_blood_request(bloodBankId, hospitalId, amount, bloodClass, bloodType, date):
    query = """INSERT INTO Orders(bloodBankId, hospitalId, amount, bloodClass, type, date) VALUES({}, {}, {}, '{}', '{}', '{}')"""
    return query.format(bloodBankId, hospitalId, amount, bloodClass, bloodType, date)
 
def order_refused(id):
    query = """UPDATE orders SET status = 'refused' WHERE id = {}"""
    return query.format(id)

def order_accepted(id):
    query = """UPDATE orders SET status = 'accepted' WHERE id = {}"""
    return query.format(id)