def blood_reauest_refused(id):
    query = """UPDATE donations SET status = 'refused' WHERE id = {}"""
    return query.format(id)


def update_user(userId, weight, hasDiseases):
    query = """UPDATE public.users SET weight={}, hasDiseases={} WHERE users.id = {}"""
    return query.format(weight, hasDiseases, userId)
