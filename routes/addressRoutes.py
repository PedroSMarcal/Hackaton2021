from flask import request
from flask_restful import Resource
from utils.addressUtils import getEspecificAddress, getAll

class AddressMethds(Resource):
    def get():
        return getAll()

    def post():
        data = request.json
        try:
            response = constructAddress(data)
        except:
            response = {'message': 'could not create the address'}
        return response
        
class AddresMethodsPa(Resource):
    def get(id):
        try:
            response = getEspecificAddress()
        except:
            response = {'message': 'address do not exists'}
        return response

