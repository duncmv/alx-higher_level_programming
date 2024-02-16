#!/usr/bin/python3
"""prints all City objects from database
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for c, s in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all():
        print(f"{s.name}: ({c.id}) {c.name}")
    session.close()
