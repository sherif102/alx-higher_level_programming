#!/usr/bin/python3
"""
Module: 13-model_state_delete_a.py
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

    for x in session.query(State).filter(State.name.contains('a')).all():
        session.delete(x)

    session.commit()
