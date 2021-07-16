from models.models import Citizen
from validate_email import validate_email
import hashlib

def getCitizen():
    citizen = Citizen.query.all()
    response = [{'name': i.email, 'password': i.password, 'fullname': i.fullname, 'cpf': i.cpf, 'whatsapp': i.whatsapp} for i in citizen if i.active == True]

    return response

def getespecificCitizen(id):
    citizen = Citizen.query.filter_by(id=id).first()
    if citizen.active == True:
        return {'email': citizen.email, 'password': citizen.password, 'fullname': citizen.fullname, 'cpf': citizen.cpf, 'whatsapp':  citizen.whatsapp}
    else:
        return {'mensagem': 'Do not find any user'}

def alterCitizen(id, data):
    try:
        citizen = Citizen.query.filter_by(id=id).first()
        if 'whatsapp' in data:
            citizen.whatsapp = data['whatsapp']
        citizen.save()       
        response = {'message': "change with success"}
    except:
        response = {
            'message': 'Pessoa not found'
        }
    return response


def constructCitizen(data):
    hash_password = encrypt_string(data['password'])
    try: 
        is_valid = validate_email(data['email'])
        try:
            new_data = Citizen(
                fullname=data['fullname'], 
                email=data['email'], 
                password=hash_password,
                cpf = data['cpf'],
                whatsapp = data['whatsapp']
            )
            new_data.save()
            response = {'message': 'Create with Success'}
        except:
            response = {'message': 'Could not create the user'}

    except:
        return {'message': 'Invalid e-mail, or already in use'}

    return response

def deleteCitizen(id):
    try:
        citizen = Citizen.query.filter_by(id=id).first()
        response = admin
    except:
        response = {'message': 'could not find the user'}
    
    return response

# {
#     "fullname": "Pedro Henrique Silva Marçal",
#     "email": "pedro.h.silva.marcal361@gmail.com",
#     "password": "Why",
#     "cpf": "46601160857",
#     "whatsapp": "16993933505"
# }

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
