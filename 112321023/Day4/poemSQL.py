import sqlite3
db_filename = 'test.db'
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

stmt = 