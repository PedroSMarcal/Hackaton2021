from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker,  relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('sqlite:///atividades.db', convert_unicode=True, echo=True)

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Admin(Base):
    __tablename__ = 'admin'
    name = Column(String(length = 50))
    chapaNumber = Column(Integer, primary_key = True, unique=True)
    email = Column(String(80), unique=True)
    password = Column(String(80))
    active = Column(Boolean(), default=True)
    admin = relationship('Password_Forgot', backref='admin', lazy=True)

    def __repr__(self):
        return f'Numero de Chapa: {self.chapaNumber}, \nEmail: {self.email}, \nPassword: {self.password}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()    