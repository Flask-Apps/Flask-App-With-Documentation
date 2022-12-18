#! bin/python

import sqlite3
# creates a connection to database file
conn = sqlite3.connect("src/people.db")

# creates a cursor from the connection
cur = conn.cursor()

# Use the cursor to execute a SQL query expressed as a string
cur.execute("SELECT * FROM person")

people = cur.fetchall()
for person in people:
    print(person)