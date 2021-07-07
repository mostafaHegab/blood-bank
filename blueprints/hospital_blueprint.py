import datetime
from db.bank_blood_request import add_new_blood_request
from flask import Blueprint, request, render_template, redirect, session
from db.init import execute
from db.hospital_data_and_blood_searching import get_hospital_data_by_email, search_for_blood
from utils.alert import alert
from utils.security import check_encrypted_password
from db.blood_requests import blood_requests_for_hospital

hospital = Blueprint('hospital', __name__)


@hospital.route('/login', methods=['POST', 'GET'])
def login():
    if(request.method == 'GET'):
        return render_template('hos_login.html')

    if (request.method == 'POST'):
        email = request.form['email']
        password = request.form['password']

        hospitals = execute(get_hospital_data_by_email(email))
        if len(hospitals) == 0:
            return alert('no hospital matches this email')
        hospital = hospitals[0]
        print(hospital)
        passwordVerified = check_encrypted_password(
            password, hospital['password'])
        if not passwordVerified:
            return alert('incorrect password')
        session['hospital'] = {
            "id": hospital['id'], "email": hospital['email']}
        return redirect('/hospital/home')


@hospital.route('/home', methods=['GET', 'POST'])
def hospital_home():
    if request.method == 'GET':
        data = session.get(
            'search', {'banks': [], 'bloodClass': '', 'bloodType': ''})
        session['search'] = {'banks': [], 'bloodClass': '', 'bloodType': ''}
        return render_template('hospital_home.html', data=data)

    if request.method == 'POST':
        banks = execute(search_for_blood(
            request.form['bloodType'], request.form['bloodClass'], session.get('hospital')['id']))
        session['search'] = {
            'banks': banks, 'bloodClass': request.form['bloodClass'], 'bloodType': request.form['bloodType']}
        return redirect('/hospital/home')


@hospital.route('/blood-request', methods=['POST'])
def request_blood():
    execute(add_new_blood_request(request.form['bankId'], session.get('hospital')['id'],
                                  request.form['count'], request.form['bloodClass'], request.form['bloodType'], datetime.datetime.now()))
    return redirect('/hospital/home')


@hospital.route('/blood-request', methods=['GET'])
def Hospital_Request_Blood():
    Hrequests = execute(blood_requests_for_hospital(
        session.get("hospital")["id"]))
    return render_template('Hos_Requests.html', Hrequests=Hrequests)
