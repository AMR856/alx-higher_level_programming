#!/usr/bin/python3
"""I'm just writing codes here nothing's new"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    myCursor = db.cursor()
    myCursor.execute("SELECT name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = %s LIMIT 1)", (sys.argv[4], ))
    myRows = myCursor.fetchall()
    count = 0
    for row in myRows:
        print(row[0], end='')
        count = count + 1
        if (count != len(myRows)):
            print(', ', end='')
    print()
    myCursor.close()
    db.close()
