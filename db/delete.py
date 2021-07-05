def delete_blood_case(id):
    query = """ update BloodCases set isDeleted = true where BloodCases.id= {} """

    return query.format(id) 
