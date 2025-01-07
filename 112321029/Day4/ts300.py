import sqlite3

db_filename = 'ts300.db'
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

with open('ts300.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
id = None
title = ""
poet = ""
poem = ""
data = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.isdigit():
        if id is not None:
            data.append((id, title, poet, poem.strip()))
        id = int(line)
        title = ""
        poet = ""
        poem = ""
    elif line.startswith("作者："):
        poet = line.replace("作者：", "").strip()
    elif "（" in line and "）" in line:
        title = line.strip()
    else:
        poem += line + "\n"

if id is not None:
    data.append((id, title, poet, poem.strip()))

for entry in data:
    id, title, poet, poem = entry
    cursor.execute(
        "INSERT INTO ts300 (id, title, poet, poem) VALUES (?, ?, ?, ?)", 
        (id, title, poet, poem)
    )
conn.commit()
conn.close()