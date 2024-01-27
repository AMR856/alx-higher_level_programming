#!/usr/bin/python3
"""Here we test relationships"""
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City
from relationship_state import Base
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    mySession = Session()

    theAddedState = State(name="California")
    TheAddedCity = City(name="San Francisco")
    theAddedState.cities.append(TheAddedCity)

    mySession.add(theAddedState)
    mySession.add(TheAddedCity)
    mySession.commit()
