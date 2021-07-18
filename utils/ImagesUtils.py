from models.models import Photos, Occurrence

import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def contructImages(f):
    obj = Occurrence.query(ObjectRes).order_by(ObjectRes.id.desc()).first()
    new_Photo = Photos({
        "name": f.filename, 
        "occurrence_id": obj.id
    })
    f.save(secure_filename(f.filename))
    response = {'message': 'upload complete'}

def getImages(id):
    obj = Photos.query.filter_by(id=id)
    return obj