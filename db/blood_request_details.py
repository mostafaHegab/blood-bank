def get_blood_request_details(order_id):
    query = """SELECT 
	Orders.id AS "Order Id",  
	Hospitals.name AS "Hospital Name",
	CONCAT(
	Governorates.name,
	', ',
	Cities.name,
	', ',
	Hospitals.street,
	' St.') AS "Hospital Address",	
	Orders.amount AS "Amount",
	Orders.date AS "Order Date"
 	FROM
	Orders
	INNER JOIN 
	Hospitals
	ON
	Orders.hospitalId = Hospitals.id
	INNER JOIN 
	Cities  
	ON 
	Hospitals.cityId = Cities.id 
	INNER JOIN 
	Governorates 
	ON Governorates.id = Cities.governorateId
	WHERE Orders.id = {}"""

    return query.format(order_id)