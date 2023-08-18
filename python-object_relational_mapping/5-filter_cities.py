#!/usr/bin/python3
"""
Lists all cities of a particular state
"""
import MySQLdb
import sys


if __name__ == '__main__':
    con = MySQLdb.connect(db=sys.argv[3], user=sys.argv[1], passwd=sys.argv[2])
    with con.cursor() as cur:
        """Used context manager to automatically close the cursor object"""
        cur.execute('''SELECT cities.name FROM cities JOIN states ON
                    states.id=cities.state_id
                    WHERE states.name = %s;''', (sys.argv[4], ))
        print(", ".join([row[0] for row in cur.fetchall()]))
    con.close()
