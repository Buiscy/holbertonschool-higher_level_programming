#!/usr/bin/python3
"""Retrieve and display states from a MySQL database."""
import sys
import MySQLdb

if __name__ == "__main__":
    sql_username = sys.argv[1]
    sql_password = sys.argv[2]
    database_name = sys.argv[3]

    dbc = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sql_username,
        passwd=sql_password,
        db=database_name
    )

    mouse = dbc.cursor()
    mouse.execute("SELECT id, name FROM states ORDER BY id ASC")
    results = mouse.fetchall()
    for result in results:
        print(result)

    mouse.close()
    dbc.close()
