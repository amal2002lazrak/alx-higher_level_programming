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

    # state to update
    update_state = session.query(State).filter_by(id=2).first()

    # update the name
    if update_state:
        update_state.name = 'New Mexico'

    # commit changes
    session.commit()
