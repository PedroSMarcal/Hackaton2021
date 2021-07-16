from flask import request
from flask_restful import Resource
from utils.AdminUtils import getAdmin, getespecificAdmin, constructAdmin

class AdminMethods(Resource):
    def get(self):
        return getAdmin()

    def post(self):
        data = request.json
        response = constructAdmin(data)
        return response

class AdminMethodsPa(Resource):
    def get(self, id):
        response = getespecificAdmin(id)
        return response

    def delete(self, id):
        id = int(id)
        print(id)
        try:
            data = getespecificAdmin(id)
            data.delete()
            response = {'message': 'deleted was success'}
        except:
            response = {'message': 'could not find the User'}    
        return response
    