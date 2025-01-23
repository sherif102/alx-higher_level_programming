#!/usr/bin/python3
"""
Model: 14-model_city_fetch_by_state.py
Author: Sheriff Abdulfatai
"""


if __name__ == "__main__":
    from sys import argv as a
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(f"mysql+mysqldb://{a[1]}:{a[2]}@localhost/{a[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).join(City).order_by(City.id).all()
    for state in query:
        for city in state.cities:
            print(f"{state.name}: ({city.id}) {city.name}")
