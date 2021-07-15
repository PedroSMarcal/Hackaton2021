from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker,  relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

#conectar com postgres
# engine = create_engine(
#     "postgresql+pg8000://scott:tiger@localhost/test",
#     execution_options={
#         "isolation_level": "REPEATABLE READ"
#     }
# )
# 
# SEGUE O MODELO DE OCMO TEM QUE SER COMPLETADO AS INFORMAÇÕES
# engine = create_engine("postgresql://(Usuarioaseusar):(senha)@localhost/(nome do banco)")

engine = create_engine('sqlite:///atividades.db', convert_unicode=True, echo=True)

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

'''
Here we will have the classes and the respectives methods
'''
#  CLASS ADMIN
class Admin(Base):
    __tablename__ = 'admin'
    name = Column(String(length = 50))
    chapaNumber = Column(Integer, primary_key = True, unique=True)
    email = Column(String(80), unique=True)
    password = Column(String(80))

    def __repr__(self):
        return f'Numero de Chapa: {self.chapaNumber}, \nEmail: {self.email}, \nPassword: {self.password}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

# CLASS CITIZEN
class Citizen(Base):
    __tablename__ = 'citizen'
    id = Column(Integer, primary_key = True)
    email = Column(String(80))
    password = Column(String(length = 80))
    fullname = Column(String(length = 80))
    cpf = Column(String(length = 11), unique=True)
    whatsapp = Column(String(length = 11), unique=True)
    pessoa = relationship('Citizen', backref="occurrence", lazy=True)
    admin = relationship('admin', backref='admin', lazy=True)

    def __repr__(self):
        return f'Nome Completo: {self.fullname}, \nEmail: {self.email}, \nPassword: {self.password}, \nCPF: {self.cpf}, \nWhatsapp: {self.whatsapp}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

# CLASS STATUS 
class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key = True)
    description = Column(String(length = 60), nullable = False)
    status = relationship('Status')

# CLASS OCCURRENCE
class Occurrence(Base):
    __tablename__ = 'occurrence'
    id = Column(Integer(), primary_key = True)
    date = Column(DateTime())
    viewed = Column(Boolean())
    auto_number = Column(Integer())
    obs = Column(String(length = 250), nullable = True)
    proper = Column(String(length = 80), nullable = True)
    cellphone = Column(String(length = 11), unique=True)

    status_id = Column(Integer, ForeignKey('status.id'), nullable=True)
    id_citizen = Column(Integer(), ForeignKey('citizen.id'))
    occurrence_admin = Column(ForeignKey('occurrence.id'), nullable=True)

    occurrence_address = relationship('Address')
    occurrence_photos = relationship('Photos')
    problem_type = relationship('Occurrence', backref='problem', lazy=True)

# CLASS FORGOT PASSWORD
class Password_Forgot(Base):
    __tablename__ = 'password_forgot'
    id = Column(Integer, primary_key = True)
    token = Column(String(length = 80))
    
    def __repr__(self):
        return f'token: {self.token}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

# CLASS FORGOT PASSWORD
class ProblemTypes(Base):
    __tablename__ = 'problem_types'
    id = Column(Integer, primary_key=True)
    description = Column(String(length = 45))
    occurrence = relationship('Occurrence', backref='problem', lazy=True)

# CLASS FORGOT PASSWORD
class OccurrenceceAdmin(Base):
    __tablename__ = 'occorrurence_admin'
    id = Column(Integer(), primary_key = True)
    occurrence_id = Column(Integer, ForeignKey('occurrence.id'))
    admin_chapanumber = Column(Integer, ForeignKey('admin.chapaNumber'))

# CLASS Address
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer(), primary_key = True)
    number = Column(String(length = 4))
    street = Column(String(length = 80))
    neighborhood = Column(String(length = 80))
    cep = Column(String(length = 80))
    occurrence_id = Column(Integer, ForeignKey('occurrence.id'))
    
# CLASS Photos
class Photos(Base):
    __tablename__ = 'occurrence_photo'
    id = Column(Integer(), primary_key = True)
    name = Column(String(length = 125))
    occurrence_id = Column(Integer, ForeignKey('occurrence.id'), nullable = False)

    
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()    