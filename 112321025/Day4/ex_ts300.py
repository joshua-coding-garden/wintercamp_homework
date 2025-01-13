import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

file = open("ts300.txt", "r", encoding="utf-8")
poems = file.read().strip().split("\n\n\n\n")

for poem in poems:    
    lines = poem.strip().split("\n")
    id = lines[0].strip()
    title = lines[1]
    poet = lines[2].replace("作者：", '')
    poem = "\n".join(line.strip() for line in lines[4:] if line.strip())

    cursor.execute('''
    INSERT INTO ts300 (id, title, poet, poem)
    VALUES (?, ?, ?, ?)
    ''', (id, title.strip(), poet.strip(), poem.strip()))

file.close()
conn.commit()
conn.close()