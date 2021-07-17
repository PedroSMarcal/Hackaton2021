from flask import request
from flask_restful import Resource
from utils.addressUtils import getEspecificAddress, getAll, constructAddress

class AddressMethds(Resource):
    def get(self):
        return getAll()

    def post(self):
        data = request.json
        try:
            response = constructAddress(data)
        except:
            response = {'message': 'could not create the address'}
        return response
        
class AddresMethodsPa(Resource):
    def get(self, id):
        try:
            response = getEspecificAddress(id)
        except:
            response = {'message': 'address do not exists'}
        return response

