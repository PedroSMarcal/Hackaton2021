from models.models import Address

def getAll():
    try:
        address = Address.query.all()
        response = [{'number': i.number, 'street': i.street, 'neighborhood': i.neighborhood, 'cep': i.cep} for i in address]
    except:
        response = {'message': 'something got wrong'}
    return response

def getEspecificAddress(id):
    try:
        address = Address.query.filter_by(id)
        response = address
    except:
        response = {'message': 'could not find any Id'}
    return response

def constructAddress(data):
    try:
        new_data = Address({
            'number': data['number'],
            'street': data['street'],
            'neighborhood': data['neighborhood'],
            'cep': data['cep'],
            'occurrence_id': data['occurrence_id']
        })
        new_data.save()
        response = {'message': 'address created success'}
    except:
        response = {'message': 'addres canot be create'}
    return response


