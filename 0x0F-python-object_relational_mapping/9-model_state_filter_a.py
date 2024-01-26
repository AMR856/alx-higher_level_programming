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

    st = session.query(State).order_by(State.id).filter(State.name.like("%a%"))
    for myState in st:
        print(f"{myState.id}: {myState.name}")
