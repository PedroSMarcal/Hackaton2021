from flask import Flask, request, session, g
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import os
from models.models import Admin, Citizen
import hashlib

from routes.ImagesRoutes import ImagesUpload, ImagesUploadPa
from routes.adminRoutes import AdminMethods, AdminMethodsPa
from routes.statusRoute import StatusMethods, StatusMethodsPa
from routes.problemTypeRoute import ProblemTypesMethods, ProblemTypesMethodsPa
from routes.passwordForgotRoutes import PasswordForgotMethods, PasswordForgotMethodsPa
from routes.citizensRoutes import CitizenMethods, CitizenMethodsPa
from routes.occurrenceRoutes import OccurrenceMethods, OccurrenceMethodsPa
from routes.valueUser import ValueEmailAdmin, ValueEmailCitizen

# from routes.loginRoutes import LoginAdmin, LoginCitizen, LogoutUser

# from flask_mail import Mail

__author__ = 'pedro marçal'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.secret_key = os.urandom(24)
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# DataBase Configuration
# app.config['UPLOAD_FOLDER'] = 'static.images'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_request
def before_request():
    g.user = None
    try:
        if 'user_id' in session:
            admin = Admin.query.filter_by(id=session['user_id']).first()
            if session['user_id'] in admin:
                user = admin.id
            g.user = user
    except:
        if 'user_id' in session:
            citizen = Citizen.query.filter_by(id=session['user_id']).first()
            if session['user_id'] in citizen:
                user = citizen.id
            g.user = user

class LoginAdmin(Resource):
    def post(self):
        session.pop('user_id', None)

        data = request.json
        
        admin = Admin.query.filter_by(email=data['email']).first()
        if admin and admin.password == encrypt_string(data['password']):
            session['user_id'] = admin.id
            return {'message': 'log in with success'}
        else:
            return {'message': 'conot log in'}

class LoginCitizen(Resource):
    def post(self):
        session.pop('user_id', None)

        data = request.json
        
        citizen = Citizen.query.filter_by(email=data['email']).first()
        if citizen and citizen.password == encrypt_string(data['password']):
            session['user_id'] = citizen.id
            return {'message': 'log in with success'}
        else:
            return {'message': 'conot log in'}

class Logout(Resource):
    def get(self):
        session.pop('user_id', None)

class profile(Resource):
    def get(self):
        if not g.user:
            return {'message': 'try to login'}


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

#Adding routes to api
api = Api(app)

# -----------IMAGES-----------
api.add_resource(ImagesUpload, '/uploader')
# api.add_resource(ImagesUploadPa, '/uploader/<id>')

#------------ADMIN-----------
api.add_resource(AdminMethods, '/admin')
api.add_resource(AdminMethodsPa, '/admin/<string:id>')

#------------CITIZEN---------
api.add_resource(CitizenMethods, '/citizen')
api.add_resource(CitizenMethodsPa, '/citizen/<string:id>')

#------------STATUS----------
api.add_resource(StatusMethods, '/status')
api.add_resource(StatusMethodsPa, '/status/<string:id>')

#------------PROBLEM TYPES------
api.add_resource(ProblemTypesMethods, '/problem')
api.add_resource(ProblemTypesMethodsPa, '/problem/<string:id>')

#------------FORGOT PASSWORD------
api.add_resource(PasswordForgotMethods, '/password')
api.add_resource(PasswordForgotMethodsPa, '/password/<string:id>')

#-----------OCURRENCE---------------
api.add_resource(OccurrenceMethods, '/occurrence')
api.add_resource(OccurrenceMethodsPa, '/occurrence/<string:id>')

# -----------LOGIN------------------
api.add_resource(LoginAdmin, '/loginadmin')
api.add_resource(Logout, '/logout')

#-----------VALUE EMAIL-------------
api.add_resource(ValueEmailAdmin, '/adminvalue/<id>')
api.add_resource(ValueEmailCitizen, '/citizenvalue/<id>')

if __name__ == '__main__':
    app.run(debug=True)


# api.add_resource(LoginAdmin, '/loginadmin')
# api.add_resource(LoginCitizen, '/logincitizen')

