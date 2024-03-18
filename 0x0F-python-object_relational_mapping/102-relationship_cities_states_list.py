#!/usr/bin/python3
""" creates a state and a city """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


def execute():
    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, pswd, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()  

    cities = session.query(City).order_by(City.id)
    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))


if __name__ == '__main__':
    execute()
