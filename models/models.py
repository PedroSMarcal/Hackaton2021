from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker,  relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///atividades.db', convert_unicode=True, echo=True)

#conectar com postgres
# engine = create_engine(
#     "postgresql+pg8000://scott:tiger@localhost/test",
#     execution_options={
#         "isolation_level": "REPEATABLE READ"
#     }
# )
# 
#  SEGUE O MODELO DE OCMO TEM QUE SER COMPLETADO AS INFORMAÇÕES
# engine = create_engine("postgresql://(Usuarioaseusar):(senha)@localhost/(nome do banco)")

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

'''
Here we will have the classes and the respectives methods
'''
#  User
class CommonUser(Data):
    __tablename__ = 'common_user'
    id = Column(Integer, primary_key = True)
    fullname = Column(String(80))
    cpf = Column(String(11))
    active = Column(Boolean)
    password = Column(String(80))
    types = Column(String(50)) 
    whatsapp = Column(String(14))
    email = Column(String(50))

    def __repr__(self):
        return f'fullname {self.fullname} \ncpf {self.cpf} \nactive {self.active} \ntypes {self.types} \nwhatsapp {self.whatsapp} \n'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class UserAdmin(Data):
    __tablename__ = 'user_admin'
    id = Column(Integer, primary_key = True)
    username = Column(String(40))
    password = Column(String(80))
    email = Column(String(50))
    status = Column(Boolean)

    def __repr__(self):
        return f'username {self.username} \nemail {self.email}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class TypeOccurence(Data):
    __tablename__ = 'type_ocurrence'
    id = Column(Integer, primary_key = True)
    types = Column(String(45))
    description = Column(String(45), nullable=False)

    def __repr__(self):
        return f'types {self.types} \ndescription {self.description}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Ocurrence(Data):
    __tablename__ = 'ocurrence'
    ocurrence_number = Column(Integer, primary_key = True)
    referenced_points = Column(String(45))
    notes = Column(String(80), nullable = False)
    status = Column(Boolean)

    def __repr__(self):
        return f'ocurrence_number {self.ocurrence_number} \nreferenced_points {self.referenced_points} \nnotes {self.Notes} \nstatus {self.status}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class User_Occurrence(Data):
    pass 