#!/usr/bin/python3
"""Starting to get something real"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    myCursor = db.cursor()
    myCursor.execute("SELECT * FROM states WHERE name LIKE %s".format('%s'), [sys.argv[4]])
    myRows = myCursor.fetchall()
    for row in myRows:
        print(row)
    myCursor.close()
    db.close()
