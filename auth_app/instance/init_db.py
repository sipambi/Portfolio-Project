import sqlite3

connection = sqlite3.connect('db.sqlite')

try:
    with open('schema.sql') as f:
        connection.executescript(f.read())
except Exception as exc:
    print("Error is because %s" % exc)