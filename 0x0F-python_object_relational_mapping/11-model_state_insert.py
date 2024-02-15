#!/usr/bin/python3
"""Adds the state Louisiana to database
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    obj = State(name='Louisiana')
    session.add(obj)
    session.commit()
    state = session.query(State).filter(State.name == 'Louisiana')
    if len(list(state)) > 0:
        print(f"{state[0].id}")
    session.close()
