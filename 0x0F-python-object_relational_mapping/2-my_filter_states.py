#!/usr/bin/python3
# a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.


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
        search=argv[4],
        charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER By states.id ASC")
    row_query = cur.fetchall()

    # printing the data
    for row in row_query:
        print(row)
    cur.close()
    con.close()
