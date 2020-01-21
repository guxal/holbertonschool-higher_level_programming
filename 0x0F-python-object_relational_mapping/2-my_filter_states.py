#!/usr/bin/python3
'''This script list states where name matches the argv[4]'''
import sys
import MySQLdb

if len(sys.argv) == 5:
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    mydb = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        database=database
    )

    mycursor = mydb.cursor()
    query = "SELECT * FROM states WHERE name='{}'".format(name)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for data in myresult:
        print(data)

    mycursor.close()
