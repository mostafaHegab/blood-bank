from flask import Blueprint, request, render_template, redirect, session

from db.init import execute
from db.user import add_user, get_user_by_email
from utils.security import encrypt_password, check_encrypted_password
from utils.alert import alert

auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET'])
def get_auth():
    return render_template('signin.html')


@auth.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']
    gender = request.form['gender']
    birthdate = request.form['birthdate']
    bloodClass = request.form['bloodClass']
    users = execute(get_user_by_email(email))
    if len(users) > 0:
        return alert('email already exists')
    password = encrypt_password(password)
    execute(add_user(name, email, password, gender, birthdate, bloodClass))
    return redirect('/auth')


@auth.route('/signin', methods=['POST'])
def signin():
    password = request.form['password']
    email = request.form['email']
    users = execute(get_user_by_email(email))
    if len(users) == 0:
        return alert('no user matches this email')
    user = users[0]
    print(user)
    passwordVerified = check_encrypted_password(password, user['password'])
    if not passwordVerified:
        return alert('incorrect password')
    session['user'] = {"id": user['id'], "name": user['name']}
    return redirect('/user')
