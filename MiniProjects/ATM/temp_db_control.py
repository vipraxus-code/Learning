import sqlite3
from pathlib import Path

path = Path(__file__).with_name("users.db")

with sqlite3.connect(path) as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
for row in cur.fetchall():
    print(row)
