from flask import request
from flask_restful import Resource
from utils.PasswordForgotUtils import getPasswords, getEspecificPassword

class PasswordForgotMethods(Resource):
    def get(self):
        try:
            response = getPasswords()
        except:
            response = {'message': 'could not find the error'}
        return response

    def post(self):
        pass

class PasswordForgotMethodsPa(Resource):
    def get(self, id):
        try:
            response = getEspecificPassword()
        except:
            response = {'message': 'something got wrong please try again later'}

    def delete(self, id):
        try:
            pass
        except:
            pass
        return response