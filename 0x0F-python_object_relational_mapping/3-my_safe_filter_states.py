#!/usr/bin/python3
"""this module safely retrieves states from a database that match a cmdline arg
using MySQLdb"""


if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    name = (argv[4],)
    query = "SELECT * FROM states WHERE states.name= %s ORDER BY states.id ASC"
    cur.execute(query, name)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
