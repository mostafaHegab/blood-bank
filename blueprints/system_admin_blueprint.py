from flask import Blueprint, request, render_template, redirect, session
from db.init import execute
from db.super_admin import add_hospitals, add_bloodbank, get_hospitals, get_bloodbanks
import datetime
from utils.alert import alert 
from utils.security import encrypt_password

sys_admin = Blueprint('sys_admin', __name__)

@sys_admin.route('/', methods=['GET'])
def adding_hos_bank():
    return render_template('add_hos_bank.html')


@sys_admin.route('/add-bloodbank', methods=['POST'])
def add_bank():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    confirmPassword = request.form['confirm password']
    phone = request.form['phone']
    street = request.form['street']
    cityId = request.form['city id']
    info = request.form['info']
    createdAt = datetime.datetime.now()
    if password == confirmPassword :
        password =encrypt_password(password)
        execute(add_bloodbank(name,email,password, phone, street, cityId, info, createdAt))
    else :
        return alert("Password isn't correct")

    return redirect('/sys-admin')
    

@sys_admin.route('/add-hospital', methods=['POST'])
def add_hos():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    confirmPassword = request.form['confirm password']
    phone = request.form['phone']
    street = request.form['street']
    cityId = request.form['city id']
    info = request.form['info']
    createdAt = datetime.datetime.now()
    if password == confirmPassword :
        password =encrypt_password(password)
        execute(add_hospitals(name,email,password, phone, street, cityId, info, createdAt))
    else :
        return alert("Password isn't correct")

    return redirect('/sys-admin')
    
@sys_admin.route('/view-banks', methods=['GET'])
def show_bank():
    banks = execute(get_bloodbanks())
    print(banks)
    return render_template('show_banks.html', banks= banks)

@sys_admin.route('/view-hospitals', methods=['GET'])
def show_hospitals():
    hospitals = execute(get_hospitals())
    return render_template('show_hospitals.html', hospitals= hospitals)
