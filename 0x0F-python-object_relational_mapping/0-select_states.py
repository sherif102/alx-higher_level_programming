#!/usr/bin/python3
"""
Module: 0-select_states.py
Author: Sheriff Abdulfatai
"""
if __name__ == "__main__":
    import MySQLdb

    try:
        db = MySQLdb.connect(user='developer',
                             passwd='Developer@123',    db='hbtn_0e_0_usa')
    except Exception as e:
        print(f"Error: {e.args[1]}")

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    for row in cur.fetchall():
        print(row)
