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

    poem_with_numbers = []
    for line in poem.split("\n"):
        if any(char.isnumeric() for char in line):
            poem_with_numbers.append(line)
    
    if poem_with_numbers:
        poem_with_numbers_str = "\n".join(poem_with_numbers)

    cursor.execute('''
    INSERT INTO ts300 (id, title, poet, poem)
    VALUES (?, ?, ?, ?)
    ''', (id, title.strip(), poet.strip(), poem_with_numbers_str.strip()))

file.close()
conn.commit()
conn.close()