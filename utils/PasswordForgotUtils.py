from models.models import Password_Forgot

def getPasswords():
    try:
        response = Password_Forgot.query.all()
    except:
        response = {'message', 'could not find any user'}
    return response

def getEspecificPassword(id):
    try:
        response = Password_Forgot.query.filter_by(id=id).first() 
    except:
        response = {'message', 'do not exhist this user on database'}
    return response

def createTokenPassword():
    pass

def constructPassword():
    pass

def deletePassword():
    pass
