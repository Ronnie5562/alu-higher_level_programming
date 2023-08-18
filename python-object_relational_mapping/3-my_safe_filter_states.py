#!/usr/bin/python3
"""
displays all values in the states table where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    con = MySQLdb.connect(db=sys.argv[3], user=sys.argv[1], passwd=sys.argv[2])
    with con.cursor() as cur:
        """Used context manager to automatically close the cursor object"""
        query = 'SELECT * FROM states WHERE name = %s ORDER BY id;'
        cur.execute(query, (sys.argv[4],))
        [print(row) for row in cur.fetchall()]
    con.close()
