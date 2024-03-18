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

    state = session.query(State).first()
    if state is not None:
        print('{}: {}'.format(state.id, state.name))
    else:
        print("Nothing")


if __name__ == '__main__':
    execute()
