#!/usr/bin/python3
"""This module manipulates data from a database"""
import MySQLdb
import sys


def selectDB():
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_PORT = 3306

    arg = sys.argv[4]
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB, port=MY_PORT)
    cursor = db.cursor()
    query = "select cities.name from cities \
            join states on states.id = cities.state_id \
            where states.name  = %s \
            order by cities.id"
    cursor.execute(query, (arg,))
    rows = cursor.fetchall()

    first = True
    for row in rows:
        for data in row:
            if not first:
                print(", ", end="")
            print(data, end="")
            first = False
    print()

    db.close()


if __name__ == "__main__":

    selectDB()
