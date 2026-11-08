#!/usr/bin/python3
"""Retrieve and display states from a MySQL database."""
import sys
import MySQLdb

if __name__ == "__main__":
    sql_usnm = sys.argv[1]
    sql_pswd = sys.argv[2]
    sql_dbnm = sys.argv[3]
    sql_qury = sys.argv[4]

    dbc = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sql_usnm,
        passwd=sql_pswd,
        db=sql_dbnm
    )

    mouse = dbc.cursor()
    mouse.execute(
                "SELECT cities.name "
                "FROM cities "
                "INNER JOIN states ON cities.state_id=states.id "
                "WHERE BINARY states.name = %s "
                "ORDER BY cities.id ASC;",
                (sql_qury,)

    )

    results = mouse.fetchall()
    result = []
    for item in results:
        result.append(item[0])
    print(", ".join(result))

    mouse.close()
    dbc.close()
