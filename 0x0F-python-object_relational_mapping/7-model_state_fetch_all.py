#!/usr/bin/python3
"""
Module: 7-model_state_fetch_all.py
Author: Sheriff Abdulfatai
"""


import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                       f"@localhost/{sys.argv[3]}", pool_pre_ping=True)

Session = sessionmaker(bind=engine)

session = Session()

for x in session.query(State).order_by(State.id):
    print(f"{x.id}: {x.name}")
