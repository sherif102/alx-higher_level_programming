#!/usr/bin/python3
"""
Module: 0-select_states.py
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
    cur.execute("SELECT cities.name FROM cities "
                "LEFT JOIN states ON states.id = cities.state_id "
                "WHERE states.name = '{}' "
                "ORDER BY cities.id".format(screener(argv[4])))
    result = []
    for row in cur.fetchall():
        result.append(row[0])
print(', '.join(result))
