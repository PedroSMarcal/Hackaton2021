from flask import request
from flask_restful import Resource
from utils.CitizensUtils import getCitizen, constructCitizen, getespecificCitizen, deleteCitizen, alterCitizen

class CitizenMethods(Resource):
    def get(self):
        return getCitizen()

    def post(self):
        data = request.json
        response = constructCitizen(data)
        return response

class CitizenMethodsPa(Resource):
    def get(self, id):
        response = getespecificCitizen(id)
        return response

    def delete(self, id):
        response = deleteCitizen(id)
        return response

    def put(self, id):
        try:
            data = request.json
            response = alterCitizen(id, data)
            return response
        except:
            return {'message': 'could not find the or alter the user'}
            

