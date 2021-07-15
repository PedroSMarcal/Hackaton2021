from models.models import Admin

def getUsers():
    admin = Admin.query.all()
    response = [{'name': i.name, 'chapaNumber': i.chapaNumber, 'email': i.email, 'password': i.password} for i in admin]

    return response

        # __tablename__ = 'admin'
    # name = Column(String(length = 50))
    # chapaNumber = Column(Integer, primary_key = True, unique=True)
    # email = Column(String(80), unique=True)
    # password = Column(String(80))
