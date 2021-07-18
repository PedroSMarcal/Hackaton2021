from flask import request
from flask_restful import Resource
from utils.StatusUtils import getAllStatus, constructStatus, deleteStatus, getSpecificStatus, deleteStatus

class StatusMethods(Resource):
    def get(self):
        return getAllStatus()

    def post(self):
        try: 
            data = request.json
            response = constructStatus(data)
        except:
            response = {'save'}
        return response

class StatusMethodsPa(Resource):
    def get(self, id):
        response = getSpecificStatus(id)
        return response

    def delete(self, id):
        try:
            status = deleteStatus(id)
            response = status
        except:
            response = {'message': 'could not delete the status'}
        return response
