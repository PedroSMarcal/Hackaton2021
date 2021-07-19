from models.models import Occurrence
from flask import send_file, send_from_directory, safe_join, abort, abort
import datetime
from utils.ImagesUtils import contructImages

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
        response = abort(400)
    return response

def getAllOccurrence():
    try:
        occurrence = Occurrence.query.all()
        response = [{'date': i.date, 'viewed': i.viewed, 'auto_number': i.auto_number, 'obs': i.obs, 'proper': i.proper, 'cellphone': i.cellphone, 'active': i.active, 'latitude': i.latitude, 'longitude': i.longitude, 'occurrenceNumber': i.occurrenceNumber, 'status_ocorrence': i.status_ocorrence, 'citizenOcurrence': i.citizenOcurrence, 'problem': i.problem} for i in occurrence]
    except:
        response = {'message': 'Somethin got wrong'}
    return response


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
