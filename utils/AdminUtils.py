from models.models import Admin
from validate_email import validate_email
import hashlib


def getAdmin():
    admin = Admin.query.all()
    response = [{'name': i.name, 'chapaNumber': i.chapaNumber, 'email': i.email, 'id': i.id} for i in admin if i.active == True]

    return response

def getespecificAdmin(id):
    admin = Admin.query.filter_by(id=id).first()
    if admin.active == True:
        return {'name': admin.name, 'chapaNumber': admin.chapaNumber, 'email': admin.email}
    else:
        return {'mensagem': 'Do not find any user'}

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
            response = {'message': 'Create with Success'}
        except:
            response = {'message': 'Could not create the user'}

    except:
        return {'message': 'Invalid e-mail, or already in use'}

    return response

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def emailSendValued(email):
    msg = Message("Hello", 
                sender="privadopedro849@gmail.com",
                recipients = [email])
    mail.send(msg)
    return 'Messge Sent '