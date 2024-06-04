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

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER,
                         passwd=MY_PASS, db=MY_DB, port=MY_PORT)
    cursor = db.cursor()
    query = "select cities.id, cities.name, states.name \
            from cities join states on cities.state_id = states.id \
            order by cities.id"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    selectDB()
