from flask import request
from flask_restful import Resource
from utils.AdminUtils import getAdmin, constructAdmin

class AdminMethods(Resource):
    def get(self):
        return getAdmin()

    def post(self):
        data = request.json
        response = constructAdmin(data)
        return response

    # def put():
    #     return ''


    # def delete():
    #     return ''
    