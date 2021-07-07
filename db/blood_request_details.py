def get_blood_request_details(order_id):
    query = """SELECT 
	Orders.id AS "orderId",  
	Hospitals.name AS "hospitalName",
	hospitals.email,
	orders.bloodClass,
	orders.type,
	CONCAT(
	Governorates.name,
	', ',
	Cities.name,
	', ',
	Hospitals.street,
	' St.') AS "hospitalAddress",	
	Orders.amount AS "amount",
	Orders.date AS "orderDate"
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
