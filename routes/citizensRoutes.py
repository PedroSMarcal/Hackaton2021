from flask import request
from flask_restful import Resource
from utils.CitizensUtils import getCitizen, constructUser

class AdminMethods(Resource):
    def get(self):
        return getCitizen()

    def post(self):
        data = request.json
        constructUser(data)
        return 'teste'

    # def put():
    #     return ''

    # def delete():
    #     return ''
    