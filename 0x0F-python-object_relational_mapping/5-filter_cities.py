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
    cities = cur.fetchall()
    cities = [city for element in cities for city in element]
    print(", ".join(cities))
    cur.close()
    db.close()
