#!/usr/bin/python3
class LockedClass:
    __slots__ = ["first_name"]


lc = LockedClass()
lc.first_name = "John"
try:
    print(lc.__dict__)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
