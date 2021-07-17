from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename
from utils.ImagesUtils import contructImages

class ImagesUpload(Resource):
    def post(self):
        data = request.json
        f = request.files['file']
        response = contructImages(f, data)
        return response

    def get(self):
        pass
