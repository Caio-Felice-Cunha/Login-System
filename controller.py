from model import Person
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib


def return_session():
    CONN = "sqlite:///loginsystem.db"
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()


class ControllerRegister:

    @classmethod
    def verify_data(cls, name, email, password):
        if len(name) > 50 or len(name) <= 1:
            return 2

        if len(email) > 200:
            return 3

        if len(password) > 100 or len(password) < 6:
            return 4

        return 1

    @classmethod
    def register(cls, name, email, password):
        session = return_session()
        user = session.query(Person).filter(Person.email == email).all()

        if len(user) > 0:
            return 5

        verified_data = cls.verify_data(name, email, password)

        if verified_data != 1:
            return verified_data

        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            new_user = Person(name=name, email=email, password=password_hash)
            session.add(new_user)
            session.commit()
            return 1  # Success
        except Exception as e:
            session.rollback()  # Rollback in case of an error
            print(f"Error occurred: {e}")
            return 6  # Custom error code for exception handling

class ControllerLogin(): 
    @classmethod
    def login(cls, email, password):
        session = return_session()
        password = hashlib.sha256(password.encode()).hexdigest()
        logged = session.query(Person).filter(Person.email == email).filter(Person.password == password).all()
        if len(logged) == 1:
            return {'logged': True,
                    'id': logged[0].id}
        
        else:
            return False
        
# print(ControllerRegister.register('Maria', 'myemail@gmail.com', 'mypassword'))

print(ControllerLogin.login('myemail@gmail.com', 'mypassword'))









