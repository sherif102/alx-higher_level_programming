#!/usr/bin/python3
"""
Module: 0-select_states.py
Author: Sheriff Abdulfatai
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3])
    except Exception as e:
        print(f"Error: {e.args[1]}")

    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name = '{}' ORDER BY id".format(argv[4]))
    for row in cur.fetchall():
        print(row)
