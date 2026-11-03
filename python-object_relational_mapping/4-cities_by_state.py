#!/usr/bin/python3
"""Retrieve and display states from a MySQL database."""
import sys
import MySQLdb

if __name__ == "__main__":
    sql_name = sys.argv[1]
    sql_pswd = sys.argv[2]
    sql_dbnm = sys.argv[3]

    dbc = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sql_name,
        passwd=sql_pswd,
        db=sql_dbnm
    )
    mouse = dbc.cursor()
    mouse.execute(
                "SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "INNER JOIN states ON cities.state_id=states.id"
                "ORDER BY cities.id ASC;"
            )

    results = mouse.fetchall()
    for result in results:
        print(result)

    mouse.close()
    dbc.close()
