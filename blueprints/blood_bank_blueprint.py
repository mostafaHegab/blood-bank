from flask import Blueprint, request, render_template, redirect, session
from db.init import execute
from db.blood_bank import get_bloodbanks_by_email
from db.bank_storage import get_bank_Storage
import datetime
from utils.alert import alert 
from utils.security import encrypt_password, check_encrypted_password
from db.donation_request import get_donation_request


bank = Blueprint('bank', __name__)

@bank.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'GET'):
        return render_template('bb_login.html')

    
    if (request.method == 'POST'):
        email = request.form['email']
        password = request.form['password']
        
        banks = execute(get_bloodbanks_by_email(email))
        if len(banks) == 0:
            return alert('no blood bank matches this email')
        bank = banks[0]
        print(bank)
        passwordVerified = check_encrypted_password(password, bank['password'])
        if not passwordVerified:
            return alert('incorrect password')
        session['bank'] = {"id": bank['id'], "email": bank['email']}
        return redirect('/bank/home')
        
        

@bank.route('/home', methods =['GET'])
def home():
    bloodcases = execute(get_bank_Storage(session.get("bank")["id"]))
    print(bloodcases)
    return render_template('Bank_home.html',bloodcases=bloodcases)

@bank.route('/request', methods=['GET'])
def show_donate_requests():
    history= execute(get_donation_request(session.get("bank")["id"]))
    print(history)
    return render_template('donate_Requests.html',history=history)

@bank.route('/manage', methods=['GET'])
def show_manage():
    
    return render_template('manage.html')

    
