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

    myState = session.query(State).filter(State.name == sys.argv[4]).first()
    if myState is None:
        print("Nothing")
    else:
        print(myState.id)
