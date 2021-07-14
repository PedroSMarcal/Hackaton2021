from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename

class ImagesUpload(Resource):
    def post(f):
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return {'message': 'the file was update with success'}

    def get():
        pass
