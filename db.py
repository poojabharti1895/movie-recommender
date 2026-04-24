import sqlite3

conn = sqlite3.connect("database/users.db")
c = conn.cursor()

c.execute("""
CREATE TABLE users (
    username TEXT,
    password TEXT
)
""")

conn.commit()
conn.close()