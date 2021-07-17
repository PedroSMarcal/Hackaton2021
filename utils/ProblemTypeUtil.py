from models.models import ProblemTypes

def getAllProblemTypes():
    try:
        problem = ProblemTypes.query.all()
        response = [{'id': i.id, 'description': i.description} for i in problem]
    except:
        reponse = {'message': 'don not exist any status to occurrence'}
    return response

def getSpecificProblemTypes(id):
    try:
        problem = ProblemTypes.query.filter_by(id=id).first()
        response = {'description': problem.description}
    except:
        response = {'message', 'could not find the status'}
    return response

def deleteProblemTypes(id):
    try:
        problem = ProblemTypes.query.filter_by(id=id).first()
        problem.delete()
        response = {'message': 'deleted with success'}
    except:
        response = {'message': 'could not find the status'}
    return response

def constructProblemTypes(data):
    try:
        new_data = ProblemTypes(
            description = data['description']
        )
        new_data.save()
        response = {'message': 'save with success'}
    except:
        response = {'message': 'could not save the status'}
    return response
