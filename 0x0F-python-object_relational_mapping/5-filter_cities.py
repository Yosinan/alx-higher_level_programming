#!/usr/bin/python3
'''
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
'''

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
        db=argv[3]
    )
    cur = con.cursor()
    cur.execute("SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s", [argv[4]])
    row_query = cur.fetchall()

    # printing the data
    k = []
    for row in row_query:
        k.append(row[0])
    print(", ".join(k))
    cur.close()
    con.close()
