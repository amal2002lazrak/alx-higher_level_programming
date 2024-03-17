#!/usr/bin/python3
"""
    Connects to a MySQL database and retrieves and prints data
    from the 'cities' table.
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # interacting with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    query = session.query(City, State) \
        .filter(City.state_id == State.id).order_by(City.id)

    # print the output
    for city, state in query:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    # commit changes
    session.commit()
