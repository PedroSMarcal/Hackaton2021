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
# engine = create_engine("postgresql://(Usuarioaseusar):(senha)@localhost/(nome do banco)")

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

'''
Here we will have the classes and the respectives methods
'''
class User(Data):
    __tablename__ = 'user'
    id = Column (Integer, Sequence('user_id_seq'),primary_key = True )
    active = Column(Boolean)
    password = Column(String(80))
    types = Column(String(50)) 

    __mapper_args__ = {
        'polymorphic_identity': 'User',
        'polymorphic_on': types
    }

class CommonUser(Data):
    __tablename__ = 'common_user'
    