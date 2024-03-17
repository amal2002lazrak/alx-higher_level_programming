#!/usr/bin/python3
"""
Define a State class
that inherits from sqlalchemy Base
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # A session is like a workspace for making changes and
    # interacting with the database.
    Session = sessionmaker(bind=engine)
    session = Session()

    # create new obj
    new_state = State(name='Louisiana')

    # add it to the session
    session.add(new_state)

    # commit changes
    session.commit()

    print(new_state.id)
