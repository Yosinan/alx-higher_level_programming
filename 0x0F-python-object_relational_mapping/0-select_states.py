#!/usr/bin/python3
# a script that lists all states from the database hbtn_0e_0_usa

import MySQLdb
from sys import argv

# the code shouldn't execute when imported
if __name__ == '__main__':
con = MySQLdb.connect(
    host='localhost',
    port=3306,
    user="root",
    passwd="root",
    db="hbtn_0e_0_usa",
    charset="utf8")
cur = con.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
row_query = cur.fetchall()

for row in row_query:
    print(row)
cur.close()
con.close()
