from flask import request
from flask_restful import Resource
from utils.ProblemTypeUtil import getAllProblemTypes, deleteProblemTypes, getSpecificProblemTypes, constructProblemTypes

class ProblemTypesMethods(Resource):
    def get(self):
        return getAllProblemTypes()

    def post(self):
        data = request.json
        response = constructProblemTypes(data)
        return response

class ProblemTypesMethodsPa(Resource):
    def get(self, id):
        response = getSpecificProblemTypes(id)
        return response

    def delete(self, id):
        try:
            status = deleteProblemTypes(id)
            response = status
        except:
            response = {'message': 'could not delete the status'}
        return response
