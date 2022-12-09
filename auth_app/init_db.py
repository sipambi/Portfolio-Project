import sqlite3

connection = sqlite3.connect('mydatabase.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO node01 (temp, hum) VALUES (?, ?)",
            ('23', '44')
            )

cur.execute("INSERT INTO node02 (temp, hum) VALUES (?, ?)",
            ('78', '32')
            )
cur.execute("INSERT INTO node03 (temp, hum) VALUES (?, ?)",
            ('23', '44')
            )

cur.execute("INSERT INTO node04 (temp, hum) VALUES (?, ?)",
            ('78', '32')
            )

connection.commit()
connection.close()