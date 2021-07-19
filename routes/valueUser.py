from flask import request
from flask_restful import Resource
from models.models import Admin, Citizen

class ValueEmailAdmin(Resource):
    def get(self, id):
        admin = Admin.query.filter_by(id=id).first()
        admin.active()

class ValueEmailAdmin(Resource):
    def get(self, id):
        citizen = Citizen.query.filter_by(id=id).first()
        citizen.active()
        