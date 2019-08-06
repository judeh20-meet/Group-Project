<<<<<<< HEAD
from model import Base, Donation 
=======
from model import Base, Donation
>>>>>>> 32f6d7bd74f04721730e3a4ee0d1df74c7df60f6

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_donation(first_name, last_name, country, city, street, house_number, email_address):
    """Add a user to the DB."""
    new_donation = Donation(first_name=first_name, last_nime=last_name, country=country, city=city, street=street, house_number=house_number, email_address=email_address)
    #there is a line of code missing here, what else does a user need?
    session.add(new_donation)
    session.commit()

