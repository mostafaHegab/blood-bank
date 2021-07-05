def blood_reauest_refused(id):
    query = """UPDATE Orders SET Orders.status = 'refused' WHERE Orders.id = {}"""
    return query.format(id)




