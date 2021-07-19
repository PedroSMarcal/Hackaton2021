from flask import request
from flask_restful import Resource
from utils.AdminUtils import getAdmin, deleteAdmin, getespecificAdmin, constructAdmin

class AdminMethods(Resource):
    def get(self):
        return getAdmin()

    def post(self):
        data = request.json
        response = constructAdmin(data)
        # teste = emailSendValued(data['email'])
        return response

class AdminMethodsPa(Resource):
    def get(self, id):
        response = getespecificAdmin(id)
        return response

    def delete(self, id):
        id = int(id)
        try:
            data = deleteAdmin(id)
            data.delete()
            response = {'message': 'deleted was success'}
        except:
            response = {'message': 'could not complete the delete'}    
        return response
    
    