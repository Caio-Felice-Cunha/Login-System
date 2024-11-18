#from tokenize import String
from sqlalchemy import create_engine, Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


CONN = "sqlite:///loginsystem.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Person(Base):
    __tablename__ = "Person"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(200))
    password = Column(String(100))


Base.metadata.create_all(engine)







