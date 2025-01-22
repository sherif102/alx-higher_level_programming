#!/usr/bin/python3
"""
Module: 10-model_state_my_get.py
Author: Sheriff Abdulfatai
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost/{sys.argv[3]}", pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    state_obj = session.query(State).filter(State.name == sys.argv[4]).\
        order_by(State.id).first()
    if state_obj:
        print(state_obj.id)
    else:
        print("Not found")
