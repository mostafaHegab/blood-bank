import psycopg2
import psycopg2.extras
import json

from utils.config import DB_CONFIG

from . import tables


def query_type(query):
    return query[:query.index(' ')].lower()


conn = psycopg2.connect(
    host=DB_CONFIG['host'],
    port=DB_CONFIG['port'],
    user=DB_CONFIG['user'],
    password=DB_CONFIG['password'],
    database=DB_CONFIG['database'],
    cursor_factory=psycopg2.extras.RealDictCursor)


def execute(query):
    c = conn.cursor()
    if query_type(query) != 'select':
        query += ' RETURNING id'
    c.execute(query)
    res = c.fetchall()
    c.close()
    conn.commit()
    return res


def insert_data():
    print('inserting data...')
    f = open('db/egypt.json',"r" ,encoding="utf-8")
    data = json.load(f)['Egypt']
    govs = 'INSERT INTO Governorates (id, name) VALUES '
    cities = 'INSERT INTO Cities (id, name, governorateId) VALUES '
    for gov in data.values():
        govName = gov['governorate_name_en'].replace('\'', ' ')
        govs += f"({gov['id']}, '{govName}'),"
        for city in gov['cities']:
            cityName = city['city_name_en'].replace('\'', ' ')
            cities += f"({city['id']}, '{cityName}', {city['governorate_id']}),"
    govs = govs[:-1]
    cities = cities[:-1]
    c = conn.cursor()
    print('inserting governorates...')
    c.execute(govs)
    print('inserting cities...')
    c.execute(cities)
    c.close()
    conn.commit()
    print('all data inserted')


def create_tables():
    print('creating tables...')
    c = conn.cursor()
    print('creating governorates table...')
    c.execute(tables.create_governorates_table())
    print('creating cities table...')
    c.execute(tables.create_cities_table())
    print('creating users table...')
    c.execute(tables.create_users_table())
    print('creating blood_banks table...')
    c.execute(tables.create_blood_banks_table())
    print('creating hospitals table...')
    c.execute(tables.create_hospitals_table())
    print('creating orders table...')
    c.execute(tables.create_orders_table())
    print('creating blood_cases table...')
    c.execute(tables.create_blood_cases_table())
    print('creating donations table...')
    c.execute(tables.create_donations_table())
    c.close()
    conn.commit()
    print('all tables created')
    insert_data()
