from models.models import Admin
from validate_email import validate_email
import hashlib

def getAdmin():
    admin = Admin.query.all()
    response = [{'name': i.name, 'chapaNumber': i.chapaNumber, 'email': i.email} for i in admin]

    return response

def constructAdmin(data):
    print(data['password'])
    hash_password = encrypt_string(data['password'])
    try: 
        is_valid = validate_email(data['email'])
        try:
            new_data = Admin(
                name=data['name'], 
                email=data['email'], 
                chapaNumber=data['chapaNumber'],
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
