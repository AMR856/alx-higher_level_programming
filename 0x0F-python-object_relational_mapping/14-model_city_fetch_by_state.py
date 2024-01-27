#!/usr/bin/python3
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    mySession = Session()

    myCities = mySession.query(City).order_by(City.id).all()
    for theCity in myCities:
        s = mySession.query(State).filter(theCity.state_id == State.id).first()
        print(f"{s.name}: ({theCity.id}) {theCity.name}")
