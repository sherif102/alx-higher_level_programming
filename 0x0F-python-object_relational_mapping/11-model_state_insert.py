#!/usr/bin/python3
"""
Module: 11-model_state_insert.py
Author: Sheriff Abdulfatai
"""

if __name__ == "__main__":
    from sys import argv as a
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(f"mysql+mysqldb://{a[1]}:{a[2]}@localhost/{a[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name='Louisiana'))
    session.commit()
    query = session.query(State).filter_by(name='Louisiana').first()
    print(query.id)
