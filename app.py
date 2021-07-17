from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from routes.ImagesRoutes import ImagesUpload
from routes.adminRoutes import AdminMethods, AdminMethodsPa
from routes.statusRoute import StatusMethods, StatusMethodsPa
from routes.problemTypeRoute import ProblemTypesMethods, ProblemTypesMethodsPa
from routes.passwordForgotRoutes import PasswordForgotMethods, PasswordForgotMethodsPa
from routes.citizensRoutes import CitizenMethods, CitizenMethodsPa
from routes.addressRoutes import AddresMethodsPa, AddressMethds
from routes.occurrenceRoutes import OccurrenceMethods, OccurrenceMethodsPa
from routes.loginRoutes import LoginAdmin, LoginCitizen, LogoutUser

# from flask_mail import Mail

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'
# DataBase Configuration
app.config['UPLOAD_FOLDER'] = 'static.images'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

api = Api(app)

lm = LoginManager()
lm.init_app(app)



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

# -----------IMAGES-----------
api.add_resource(ImagesUpload, '/uploader')

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

#-----------ADDRESS----------------
api.add_resource(AddressMethds, '/address')
api.add_resource(AddresMethodsPa, '/address/<string:id>')

#-----------OCURRENCE---------------
api.add_resource(OccurrenceMethods, '/occurrence')
api.add_resource(OccurrenceMethodsPa, '/occurrence/<string:id>')

#-----------LOGIN------------------
api.add_resource(LoginAdmin, '/loginadmin')
api.add_resource(LoginCitizen, '/logincitizen')
api.add_resource(LogoutUser, '/logout')

if __name__ == '__main__':
    app.run(debug=True)