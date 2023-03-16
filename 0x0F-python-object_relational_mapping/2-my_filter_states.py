#!/usr/bin/python3
# a script that lists all states from the database hbtn_0e_0_usa

import MySQLdb
from sys import argv

# the code shouldn't execute when imported

if __name__ == '__main__':
    # making a connection to the database
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER By id ASC")
    row_query = cur.fetchall()

    # printing the data
    for row in row_query:
        print(row)
    cur.close()
    con.close()
