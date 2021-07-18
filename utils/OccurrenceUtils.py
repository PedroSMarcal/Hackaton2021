from models.models import Occurrence
import datetime

def getAllOccurrence():
    try:
        occurrence = Occurrence.query.all()
        response = [{'date': i.date, 'viewed': i.viewed, 'auto_number': i.auto_number, 'obs': i.obs, 'proper': i.proper, 'cellphone': i.cellphone, 'active': i.active} for i in occurrence]
    except:
        response = {'message': 'Somethin got wrong'}
    return response

def getEspecificOccurrence(id):
    try:
        occurrence = Occurrence.query.filter_by(id=id).first()
        occurrence.viewed()
        response = {
            'id': occurrence.id,
            'date': occurrence.date, 
            'viewed': occurrence.viewed, 
            'auto_number': occurrence.auto_number, 
            'obs': occurrence.obs, 
            'proper': occurrence.proper, 
            'cellphone': occurrence.cellphone, 
            'status_ocorrence': occurrence.occurrence_status,
            'passwordAdmin': occurrence.admin_id
        }

    except:
        response = {'message': 'something got wrong'}
    return response

def constructOccurrence(data):
    try:
        # if data['occurrence_status'] == 0 or data['occurrence_status'] == 2:
        #     pass

        # new_date = data['date']
        # date = datetime.date(date)
        occurrence = Occurrence(
            date = data['date'], 
            hour = data['hour'],
            obs = data['obs'], 
            proper = data['proper'], 
            cellphone = data['cellphone'], 
            street = data['street'],
            number = data['number'],
            latitude = data['latitude'],
            longitude = data['longitude'],
            occurrenceNumber = data['occurrenceNumber'],
            status_ocorrence = data['status_ocorrence'],
            citizenOcurrence = data['citizenOcurrence'],
            problem = data['problem']
        )
        occurrence.save()
        response = {'message': 'created with success'}
    except:
        response = {'message': 'canot create the occurrence'}
    return response

    # class Occurrence(Base):
    # __tablename__ = 'occurrence'
    # id = Column(Integer(), primary_key = True)
    # date = Column(String(length = 10))
    # hour = Column(String(length = 5))
    # viewed = Column(Boolean(), default = False)
    # auto_number = Column(Integer(), nullable = True)
    # obs = Column(String(length = 250), nullable = True)
    # proper = Column(String(length = 80), nullable = True)
    # cellphone = Column(String(length = 11), unique = True)
    # active = Column(Boolean(), default=True)
    # number = Column(String(length = 4), nullable=False)
    # street = Column(String(length = 80), nullable=False)
    # latitude = Column(Float(), nullable=True)
    # longitude = Column(Float(), nullable=True)
    # occurrenceNumber = Column(String(length = 9), nullable = False)

    # occurrenceType = Column(Integer(), ForeignKey('problem_types.id'), nullable=True)
    # occurrence_status = Column(Integer(), ForeignKey('status.id'), nullable=False)
    # citizen_id = Column(Integer(), ForeignKey('citizen.id'), nullable=False)
    
    # occurrence_photos = relationship('Photos', backref='photos', lazy=True)


def putOccurrence(id, data):
    try:
        occurrence = Occurrence.query.filter_by(id=id).first()
        if 'auto_number' in data:
            occurrence.auto_number = data['auto_number']

        if 'obs' in data:
            occurrence.obs = data['obs']

        if 'occurrence_status' in data:
            occurrence.occurrence_status = data['occurrence_status']

        occurrence.save()
        response = {'message': "change with success"}
    except:
        response = {'message': "something got wrong change the occurrence"}
    return response

def deleteOccurrence(id):
    try:
        occurrence = Occurrence.query.filter_by(id=id).first()
        occurrence.delete()
        response = {'message': 'deleted with success'}
    except:
        response = {'message': 'canot delete the occurrence'}
    return response
