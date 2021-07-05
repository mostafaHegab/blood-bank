def update_blood_cases(orderId,setOfIds):
 query = """UPDATE public.BloodCases SET orderId={} WHERE BloodCases.id IN {}"""
 return query.format(orderId,setOfIds)