from flask import request, abort
from flask_restful import Resource
from utils.AdminUtils import getAdmin, deleteAdmin, getespecificAdmin, constructAdmin, alterAdmin

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
    
    def put(self, email):
        try: 
            data = request.json
            reponse = alterAdmin(email, data)
        except:
            abort(400)
        return response
    