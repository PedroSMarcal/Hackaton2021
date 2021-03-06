from flask import request
import os
from flask_restful import Resource
from werkzeug.utils import secure_filename
from utils.ImagesUtils import contructImages, getImages, geter

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class ImagesUpload(Resource):
    def get(self):
        return geter()

    def post(self):
        target = os.path.join(APP_ROOT, 'images/')

        if not os.path.isdir(target):
            os.mkdir(target)
        
        for file in request.files.getlist("file"):
            filename = file.filename
            try:
                response = contructImages(f)
            except:
                reponse = {'message': 'failed to save'}      

            destination = "/".join([target, filename])
            file.save(destination)
        return {'message': 'upload complete'}


class ImagesUploadPa(Resource):
    def get(self, id):      
        data = request.json
        f = request.files['file']
        response = contructImages(f, data)
        return response