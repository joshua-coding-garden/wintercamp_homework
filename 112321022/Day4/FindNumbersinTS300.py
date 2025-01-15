import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

stmt = "SELECT id, poem FROM ts300"
cursor.execute(stmt)

for id, poem in cursor.fetchall():
    ch =[]
    for i in poem:
        if i.isnumeric():
            ch.append(i)
    if ch:
        ch = ",".join(ch)
        print("id:{} word:{}". format(id, ch))
conn.close()