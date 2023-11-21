#!/usr/bin/python3
""" A script to delete all State objects with a name
    containing the letter `a` from the database hbtn_0e_6_usa """

import sys
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ This script deletes the State objects on the database """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.contains("a"))
    deleted = states.delete(synchronize_session='fetch')
    session.commit()
    session.close()
