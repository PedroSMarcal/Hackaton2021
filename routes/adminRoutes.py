from flask import request
from flask_restful import Resource
from utils.AdminUtils import getUsers

class AdminMethods(Resource):
    # def post():
    #     return ''

    # def put():
    #     return ''

    def get(self):
        return getUsers()

    # def delete():
    #     return ''
    