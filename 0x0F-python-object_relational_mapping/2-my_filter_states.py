#!/usr/bin/python3
"""this module retrieves states from a database that match a cmdline arg
using MySQLdb"""


if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE states.name='{}'
                ORDER BY states.id ASC""".format(argv[4]))
    rows = cur.fetchall()
    if len(rows) != 0:
        for row in rows:
            print(row)
    cur.close()
    db.close()
