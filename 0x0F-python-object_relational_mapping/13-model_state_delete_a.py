#!/usr/bin/python3
"""
Script that deletes all the State objects that contain letter 'a' from
the database - Using module SQLAlchemy
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session instance
    session = Session()
    Base.metadata.create_all(engine)

    del_st = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for state_delete in del_st:
        session.delete(state_delete)
    session.commit()
    session.close()
