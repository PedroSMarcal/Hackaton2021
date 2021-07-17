from models.models import Status

def getAllStatus():
    try:
        status = Status.query.all()
        response = [{'id': i.id, 'description': i.description} for i in status]
    except:
        reponse = {'message': 'don not exist any status to occurrence'}
    return response

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