#!/usr/bin/python3
"""Retrieve and display states from a MySQL database."""
import sys
import MySQLdb

if __name__ == "__main__":
    sql_usnm = sys.argv[1]
    sql_pswd = sys.argv[2]
    sql_dtbs = sys.argv[3]
    sql_input = sys.argv[4]

    dbc = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sql_usnm,
        passwd=sql_pswd,
        db=sql_dtbs
    )
    mouse = dbc.cursor()
    mouse.execute(
            (
                "SELECT id, name FROM states "
                "WHERE BINARY name = '{}' "
                "ORDER BY id ASC;"
            ).format(sql_input)
        )
    results = mouse.fetchall()
    for result in results:
        print(result)

    mouse.close()
    dbc.close()
