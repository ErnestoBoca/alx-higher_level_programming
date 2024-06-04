#!/usr/bin/python3
"""this module  lists all State objects from the database hbtn_0e_6_us"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def execute():
    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]
    host = "localhost"
    port = 3306

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           user, pswd, host, port, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = sys.argv[4]
    state = session.query(State).filter(State.name == state).first()

    if state is not None:
        print(state.id)
    else:
        print('Not found')


if __name__ == '__main__':
    execute()
