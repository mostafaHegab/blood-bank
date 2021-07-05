from flask import Blueprint, request, render_template, redirect, session
from db.init import execute
from db.hospital_data_and_blood_searching import get_hospital_data_by_email
from utils.alert import alert
from utils.security import check_encrypted_password

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
