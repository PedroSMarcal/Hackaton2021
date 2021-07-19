from flask import request, abort
from flask_restful import Resource
from utils.OccurrenceUtils import deleteOccurrence, putOccurrence, constructOccurrence, getEspecificOccurrence, getAllOccurrence
from utils.ImagesUtils import contructImages
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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
            target = os.path.join(APP_ROOT, 'images/')

            if not os.path.isdir(target):
                os.mkdir(target)
            
            for file in request.files.getlist("file"):
                filename = file.filename
                try:
                    response = contructImages(file)
                except:
                   abort(400)      

                destination = "/".join([target, filename])
                file.save(destination)

            response = constructOccurrence(data)
        except:
            response = abort(500)
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