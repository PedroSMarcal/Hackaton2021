from models.models import Photos, Occurrence
from flask import send_file, send_from_directory, safe_join, abort

import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def contructImages(f):
    obj = Occurrence.query(ObjectRes).order_by(ObjectRes.id.desc()).first()
    try:
        new_Photo = Photos({
            "name": f.filename, 
            "occurrence_id": obj.id
        })
        new_Photo.save()
        f.save(secure_filename(f.filename))
    except:
        return  abort(500)
    response = {'message': 'upload complete'}

def getImages(id):
    obj = Photos.query.filter_by(id=id)
    for i in obj:
        try:
            response =  send_from_directory(APP_ROOT, filename=obj.name, as_attachment=True)
        except FileNotFoundError:
            abort(404)
    return {'message': 'success'}


