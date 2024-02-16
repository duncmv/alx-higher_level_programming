#!/usr/bin/python3
"""prints id of state that matches name using SQLAlchemy
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    name = sys.argv[4]
    session = Session(engine)
    state = session.query(State).filter(State.name == name)
    if len(list(state)) > 0:
        print(f"{state[0].id}")
    else:
        print("Not found")
    session.close()
