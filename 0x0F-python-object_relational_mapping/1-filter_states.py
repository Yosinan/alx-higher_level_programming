#!/usr/bin/python3
# a script that lists all states with a name starting with N (upper N)
# from the database hbtn_0e_0_usa

import MySQLdb
from sys import argv

# the code shouldn't execute when imported

if __name__ == '__main__':
    # making a connection to the database
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM states WHERE nameLIKE BINARY 'N%' ORDER By id ASC")
    row_query = cur.fetchall()

    # printing the data
    for row in row_query:
        print(row)
    # cleaning up the process
    cur.close()
    con.close()
