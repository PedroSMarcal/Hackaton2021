from models.models import Admin
from validate_email import validate_email
import hashlib
from utils.emailsendAdmin import emailsend


def getAdmin():
    admin = Admin.query.all()
    response = [{'name': i.name, 'chapaNumber': i.chapaNumber, 'email': i.email, 'id': i.id} for i in admin if i.active == False ]

    return response

def alterAdmin(email, data):
    try:
        admin = Admin.query.filter_by(email=email).first()
        if 'password' in data:
            admin.password = data['password']
        
        admin.save()       
        response = {'message': "change with success"}
    except:
        response = {
            'message': 'Pessoa not found'
        }
    return response

def getespecificAdmin(id):
    try:
        Admin.load_user(id)
        admin = Admin.query.filter_by(id=id).first()
        if admin.active == False:
            response = {'name': admin.name, 'chapaNumber': admin.chapaNumber, 'email': admin.email}
        else:
            response = {'mensagem': 'Do not find any user'}
    except:
        response = {'message': 'do not find the user'}
    return response

def deleteAdmin(id):
    try:
        admin = Admin.query.filter_by(id=id).first()
        response = admin
    except:
        response = {'message': 'could not find the user'}
    
    return response


def constructAdmin(data):
    hash_password = encrypt_string(data['password'])
    try: 
        is_valid = validate_email(data['email'])
        try:
            new_data = Admin(
                name=data['name'], 
                email=data['email'], 
                password=hash_password
            )
            new_data.save()

            obj = Admin.query(ObjectRes).order_by(ObjectRes.id.desc()).first()
            response = obj.id
            # emailsend(obj.email, obj.id)

            # response = {'message': 'Create with Success'}
        except:
            response = {'message': 'Could not create the user'}

    except:
        return {'message': 'Invalid e-mail, or already in use'}

    return response

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
