#!/usr/bin/python3
"""
Model: 100-relationship_states_cities.py
Author: Sheriff Abdulfatai
"""


if __name__ == "__main__":
    from sys import argv as a
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(f"mysql+mysqldb://{a[1]}:{a[2]}@localhost/{a[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    city = City(name='San Francisco')
    city.state = State(name='California')
    session.add(city)
    session.commit()
