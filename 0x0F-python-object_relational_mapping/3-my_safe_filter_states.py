#!/usr/bin/python3
"""
Module: 3-my_safe_filter_states.py
Author: Sheriff Abdulfatai
"""


def screener(data):
    """ screens the data input into the database statement """
    lookup = ['"', "'", ';']
    screened = []
    for x in data:
        if x in lookup:
            screened.append('\\')
        screened.append(x)
    return ''.join(screened)


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
                "WHERE BINARY name = '{}' "
                "ORDER BY id".format(screener(argv[4])))
    for row in cur.fetchall():
        print(row)
