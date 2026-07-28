import sqlite3

conn = sqlite3.connect("sample.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
id INTEGER PRIMARY KEY,
name TEXT,
city TEXT
)
""")

cursor.execute("""
INSERT INTO customers(name,city)
VALUES
('Archana','Bangalore'),
('Rahul','Mysore'),
('Priya','Chennai')
""")

conn.commit()

print("Database Created Successfully")

conn.close()
import sqlite3

conn = sqlite3.connect("sample.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM customers")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()