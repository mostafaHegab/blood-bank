from db.get_blood_cases import get_blood_cases
from db.blood_request_details import get_blood_request_details
from utils.blood import expiration_date
from db.blood_case_insertion import insert_blood_case
from db.refused_requests import blood_reauest_refused, update_user
from flask import Blueprint, request, render_template, redirect, session
from db.init import execute
from db.blood_bank import get_bloodbanks_by_email
from db.bank_storage import get_bank_Storage
import datetime
from utils.alert import alert
from utils.security import encrypt_password, check_encrypted_password
from db.donation_request import get_donation_request, get_donation_details, accept_donation_request

from db.unserved_blood_requests import get_unserved_requests
from db.delete import delete_blood_case
from db.refused_requests import blood_reauest_refused
from db.bank_blood_request import order_refused, order_accepted
from db.update_blood_cases import update_blood_cases

bank = Blueprint('bank', __name__)


@bank.route('/login', methods=['POST', 'GET'])
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


@bank.route('/home', methods=['GET'])
def home():
    bloodcases = execute(get_bank_Storage(session.get("bank")["id"]))
    return render_template('Bank_home.html', bloodcases=bloodcases)


@bank.route('/home/<int:id>', methods=['POST'])
def delete(id):
    execute(delete_blood_case(id))
    return redirect('/bank/home')


@bank.route('/donation-request', methods=['GET'])
def show_donate_requests():
    history = execute(get_donation_request(session.get("bank")["id"]))
    return render_template('donate_Requests.html', history=history)


@bank.route('/donation-request/<int:rid>', methods=['GET'])
def show_donate_manage(rid):
    donationRequest = execute(get_donation_details(rid))[0]
    return render_template('Manage.html', donation=donationRequest)


@bank.route('/donation-request/<int:rid>/refuse', methods=['POST'])
def refuse_donation_request(rid):
    execute(update_user(
        request.form['userId'], request.form['weight'], request.form['hasDiseases']))
    execute(blood_reauest_refused(rid))
    return redirect('/bank/donation-request')


@bank.route('/donation-request/<int:rid>/accept', methods=['POST'])
def accept_donate_request(rid):
    execute(accept_donation_request(rid, datetime.datetime.now()))
    execute(insert_blood_case(rid, session.get("bank")["id"], request.form['bloodType'],
                              request.form['bloodClass'], datetime.datetime.now(),
                              datetime.datetime.now() + datetime.timedelta(expiration_date(request.form['bloodType']))))
    return redirect('/bank/donation-request')


@bank.route('/blood-request', methods=['GET'])
def show_blood_requests():
    requests = execute(get_unserved_requests(session.get("bank")["id"]))
    return render_template('blood_requests.html', requests=requests)


@bank.route('/blood-request/<int:rid>', methods=['GET'])
def blood_request_details(rid):
    bloodRequest = execute(get_blood_request_details(rid))[0]
    cases = execute(get_blood_cases(session.get(
        'bank')['id'], bloodRequest['bloodclass'], bloodRequest['type']))
    return render_template('manage_request.html', data={'request': bloodRequest, 'cases': cases})


@bank.route('/blood-request/<int:rid>/refuse', methods=['POST'])
def refuse_order_blood_request(rid):
    x = execute(order_refused(rid))
    print(x)
    return redirect('/bank/blood-request')


@bank.route('/blood-request/<int:rid>/accept', methods=['POST'])
def accept_order_request(rid):
    print(request.form["caseid"])
    print(request.form.getlist("caseid"))
    caseids = '(' + ','.join(request.form.getlist('caseid')) + ')'
    print(caseids)
    print(update_blood_cases(rid, caseids))
    execute(update_blood_cases(rid, caseids))
    execute(order_accepted(rid))
    return redirect('/bank/blood-request')
