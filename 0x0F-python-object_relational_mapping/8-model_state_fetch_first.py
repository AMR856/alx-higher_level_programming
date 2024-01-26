#!/usr/bin/python3
"""Another code here"""
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.id == 1).all()
    if (len(states) == 1):
        for myState in states:
            print(f"{myState.id}: {myState.name}")
    else:
        print("Nothing")
