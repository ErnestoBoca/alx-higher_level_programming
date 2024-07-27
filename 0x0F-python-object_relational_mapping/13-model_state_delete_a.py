#!/usr/bin/python3
"""This module adds a State to the database hbtn_0e_6_usa"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def execute():
    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, pswd, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))

    if states is not None:
        for state in states:
            session.delete(state)
        session.commit()


if __name__ == '__main__':
    execute()
