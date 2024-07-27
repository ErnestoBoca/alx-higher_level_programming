#!/usr/bin/python3
""" creates a state and a city """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def execute():
    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, pswd, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    san_fra = City(name='San Francisco')
    cali = State(name='California', cities=[san_fra])

    session.add(san_fra)
    session.add(cali)
    session.commit()


if __name__ == '__main__':
    execute()
