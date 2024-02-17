#!/usr/bin/python3
"""this module retrieves cities from a particlar state
from a database using MySQLdb"""


if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = """SELECT cities.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name = %s"""
    name = (argv[4],)
    cur.execute(query, name)
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i != len(rows) - 1:
            print(f"{rows[i][0]}, ", end="")
        else:
            print(f"{rows[i][0]}")
    cur.close()
    db.close()
