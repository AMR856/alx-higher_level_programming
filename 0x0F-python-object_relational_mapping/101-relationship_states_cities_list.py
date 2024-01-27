#!/usr/bin/python3
"""Here is another code"""
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

    for myObject in session.query(State).order_by(State.id):
        print(f"{myObject.id}: {myObject.name}")
        for city in myObject.cities:
            print(f"    {city.id}: {city.name}")
