#!/usr/bin/python3
"""Creates a state with related citiesusing SQLAlchemy
"""
if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    cali = State(name="California")
    cali.cities.append(City(name="San Fancisco"))
    session.add(cali)
    session.commit()
    session.close()
