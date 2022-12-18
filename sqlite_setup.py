#! bin/python

import sqlite3

conn = sqlite3.connect("src/people.db") # creates the file
columns = [
"id INTEGER PRIMARY KEY",
"lname VARCHAR UNIQUE",
"fname VARCHAR",
"timestamp DATETIME",
]
create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
conn.execute(create_table_cmd)

# conn = sqlite3.connect("src/people.db")
people = [
    "1, 'Fairy', 'Tooth', '2022-10-08 09:15:10'",
    "2, 'Ruprecht', 'Knecht', '2022-10-08 09:15:13'",
    "3, 'Bunny', 'Easter', '2022-10-08 09:15:27'",
]

for person_data in people:
    insert_cmd = f"INSERT INTO person VALUES ({person_data})"
    # create sqlite3.Cursor object in memory
    conn.execute(insert_cmd)
# to make the transaction happen (i.e insert people_data into person table)
conn.commit()