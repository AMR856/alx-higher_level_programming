#!/usr/bin/python3
"""Starting to get something real"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    myC = db.cursor()
    myC.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    myRows = myC.fetchall()
    for row in myRows:
        print(row)
    myC.close()
    db.close()
