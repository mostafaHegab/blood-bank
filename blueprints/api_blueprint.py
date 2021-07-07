import datetime
from db.bank_blood_request import add_new_blood_request
from utils.config import ACCESS_TOKEN_EXPIRATION_OFFSET, JWT_SECRET_KEY
from flask import Blueprint, request, jsonify
from db.init import execute
from db.hospital_data_and_blood_searching import get_hospital_data_by_email, search_for_blood
from utils.security import check_encrypted_password
import jwt
from utils.guards import token_required
from db.blood_requests import blood_requests_for_hospital


api = Blueprint('api', __name__)


@api.route('/hospital/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    hospitals = execute(get_hospital_data_by_email(email))
    if len(hospitals) == 0:
        return jsonify({'message': 'no account matches this email'}), 404
    hospital = hospitals[0]
    passwordVerified = check_encrypted_password(
        password, hospital['password'])
    if not passwordVerified:
        return jsonify({'message': 'wrong password'}), 406
    access_token_exp = datetime.datetime.utcnow(
    ) + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRATION_OFFSET)
    access_token = jwt.encode(
        {'id': hospital['id'], 'email': hospital['email'], 'exp': access_token_exp}, JWT_SECRET_KEY, algorithm='HS256')
    return jsonify({'access_token': access_token, 'access_token_exp': access_token_exp}), 200


@api.route('/search-blood', methods=['POST'])
@token_required
def hospital_home(hid):
    print(hid)
    banks = execute(search_for_blood(
        request.json['bloodType'], request.json['bloodClass'], hid))
    return jsonify(banks)


@api.route('/hospital/blood-request', methods=['POST'])
@token_required
def request_blood(hid):
    bloodRequest = execute(add_new_blood_request(request.json['bankId'], hid, request.json['count'],
                                                 request.json['bloodClass'], request.json['bloodType'],
                                                 datetime.datetime.now()))
    return jsonify({'id': bloodRequest[0]['id']})


@api.route('/hospital/blood-request', methods=['GET'])
@token_required
def Hospital_Request_Blood(hid):
    Hrequests = execute(blood_requests_for_hospital(hid))
    return jsonify(Hrequests)
