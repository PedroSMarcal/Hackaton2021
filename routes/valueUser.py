from flask import request
from flask_restful import Resource
from models.models import Admin, Citizen

class ValueEmailAdmin(Resource):
    def get(self, id):
        try:
            admin = Admin.query.filter_by(id=id).first()
            admin.active()
            return {'message': 200}
        except:
            return {'message': 400}
class ValueEmailCitizen(Resource):
    def get(self, id):
        citizen = Citizen.query.filter_by(id=id).first()
        citizen.active()
        