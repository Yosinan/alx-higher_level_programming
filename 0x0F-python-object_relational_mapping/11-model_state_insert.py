#!/usr/bin/python3
"""
Script that insert/adds the state object "Louisiana" to
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

    louis = State(name="Louisiana")
    session.add(louis)
    session.commit()
    # print before closing the session
    print(louis.id)
    session.close()
