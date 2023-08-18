#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    conn = MySQLdb.connect(db=sys.argv[3], user=sys.argv[1], passwd=sys.argv[2])
    with conn.cursor() as cur:
        """Used context manager to automatically close the cursor object"""
        cur.execute('SELECT * FROM states ORDER BY states.id;')
        [print(row) for row in cur.fetchall()]
    conn.close()
