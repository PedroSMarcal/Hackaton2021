from flask import request
from flask_login import login_user, logout_user
from flask_restful import Resource
import hashlib
from models.models import Admin, Citizen

class LoginCitizen(Resource):
    def post(self):
        form = request.json
        user = Citizen.query.filter_by(email=form['email']).first()
        hashed_passwords = encrypt_string(form['password'])
        if user and user.password == hashed_passwords and user.active == False:
            login_user(user)
            response = {'message': 'valid user'}
        else:
            response = {'message': 'invalid user'}
        return response

class LoginAdmin(Resource):
    def post(self):
        form = request.json
        user = Admin.query.filter_by(email=form['email']).first()
        hashed_passwords = encrypt_string(form['password'])
        if user and user.password == hashed_passwords:
            login_user(user)
            response = {'message': 'valid user'}
        else:
            response = {'message': 'invalid user'}
        return response

class LogoutUser(Resource):
    def get(self):
        try:
            logout_user()
            response = {'messge': 'Logout with success'}
        except:
            response = {'message': 'No user to logout'} 
        return response


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
