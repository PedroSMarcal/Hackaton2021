from models.models import Status
from flask import session, g

def getAllStatus():
    if not g.user:
        try:
            status = Status.query.all()
            response = [{'id': i.id, 'description': i.description} for i in status]
        except:
            response = {'message': 'don not exist any status to occurrence'}
        return response
        return {'message': 'try to login'}

def getSpecificStatus(id):
    try:
        status = Status.query.filter_by(id=id).first()
        response = {'description': status.description}
    except:
        response = {'message', 'could not find the status'}
    return response

def deleteStatus(id):
    try:
        status = Status.query.filter_by(id=id).first()
        status.delete()
        response = {'message': 'deleted with success'}
    except:
        response = {'message': 'could not find the status'}
    return response

def constructStatus(data):
    try:
        new_data = Status(
            description = data['description']
        )
        new_data.save()
        response = {'message': 'save with success'}
    except:
        response = {'message': 'could not save the status'}
    return response
