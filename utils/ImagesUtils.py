from models.models import Photos

def contructImages(f, data):
    try: 
        new_Photo = Photos({
            "name": f.filename, 
            "occurrence_id": data['occurrence_id']
        })
        f.save(secure_filename(f.filename))
        response = {'message': 'upload complete'}
    except:
        reponse = {'message': 'cant upload image'}

