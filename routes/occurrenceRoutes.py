from flask import request
from flask_restful import Resource
from utils.OccurrenceUtils import deleteOccurrence, putOccurrence, constructOccurrence, getEspecificOccurrence, getAllOccurrence

class OccurrenceMethods(Resource):
    def get(self):
        try:
            response = getAllOccurrence()
        except:
            response = {'message': 500}
        return response

    def post(self):
        try:
            data = request.json
            response = constructOccurrence(data)
        except:
            response = {'message': 500}
        return response

class OccurrenceMethodsPa(Resource):
    def get(self, id):
        try:
            response = getEspecificOccurrence()
        except:
            response = {'message': 500}
        return response

    def put(self, id):
        try:
            data = request.json
            response = putOccurrence(id, data)
        except:
            response = {'message': 500}
        return response

    def delete(self, id):
        try:
            response = deleteOccurrence(id)
        except:
            response = {'message': 500}
        return response