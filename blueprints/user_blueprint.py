from flask import Blueprint, request, render_template, redirect, session
from db.init import execute
import datetime

from db.user_donations import get_user_donations, add_user_donations, update_user
from db.user_donations import get_bloodbanks

user = Blueprint('user', __name__)


@user.route('/', methods=['GET'])
def show_donation():
    donations = execute(get_user_donations(session.get("user")["id"]))
    print(donations)
    return render_template('user_home.html', donations=donations)


@user.route('/donate', methods=['GET'])
def show_apply_donation():
    banksname = execute(get_bloodbanks())
    return render_template('donate.html', banksname=banksname)


@user.route('/donate', methods=['POST'])
def donate():
    userId = session.get("user")["id"]
    lastTreatmentDate = request.form['lastTreatmentDate']
    weight = request.form['weight']
    hasDiseases = request.form['hasDiseases']
    donationDate = request.form['donationDate']
    createdAt = datetime.datetime.now()
    bankId = request.form['bankId']
    bloodType = request.form['bloodType']
    execute(update_user(weight, hasDiseases,
            lastTreatmentDate, userId, donationDate))
    execute(add_user_donations(userId, bankId, bloodType, createdAt))

    return redirect('/user')
