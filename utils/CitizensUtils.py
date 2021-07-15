from models.models import Citizen

def getCitizen():
    citizen = Citizen.query.all()
    response = [{'name': i.email, 'password': i.password, 'fullname': i.fullname, 'cpf': i.cpf, 'whatsapp': i.cpf, 'pessoa': i.pessoa} for i in citizen]

    return response

def constructUser(data):
    print(data['password'])