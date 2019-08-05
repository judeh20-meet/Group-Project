from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()

class Donation(Base):
    __tablename__ = "donations"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    country = Column(String)
    city = Column(String)
    street = Column(String)
    house_number = Column(Integer)
    email_address = Column(String)