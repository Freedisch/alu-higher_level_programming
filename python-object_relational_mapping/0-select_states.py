#!/usr/bin/python3
"""Selecting all the states form hbtn_0e_0usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user= sys.argv[1], password=sys.argv[2], db=sys.argv[3])

    launcher = db.cursor()
    launcher.execute("SELECT * FROM states ORDER BY sates.id;")
    rows = launcher.fetchall()
    for row in rows:
        print(row)
