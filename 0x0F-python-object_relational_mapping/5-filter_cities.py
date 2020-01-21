#!/usr/bin/env python3
'''This script list states where name matches the argv[4]'''
import sys
import MySQLdb

if len(sys.argv) == 5:
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    mydb = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        database=database
    )

    mycursor = mydb.cursor()

    query = "SELECT c.name\
             FROM states AS s\
             INNER JOIN cities AS c\
             ON (c.state_id = s.id)\
             WHERE s.name = %(statename)s"

    mycursor.execute(query, {'statename': state_name})
    myresult = mycursor.fetchall()

    for i in range(len(myresult)):
        print(myresult[i][0], end=", " if i != len(myresult) - 1 else "\n")
    mycursor.close()
