import sqlite3

db_filename = 'sql/test.db'
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

fn = 'ts300.txt'
infile = open(fn, 'r', encoding='utf-8')
lines = infile.readlines()

poem_content = []
s = []
title_line, poet_line, change = None, None, None
id, title, poet, poem = None, None, None, None

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    if(lines[i] == ''):
        continue
    if(lines[i].isdigit()):
        if(id != None):
            poem = "".join(poem_content)
            s.append(f"INSERT INTO ts300 VALUES({id}, '{title}', '{poet}', '{poem}')")
            poem_content = []
        id = int(lines[i])
        title_line = i + 1
    elif(i == title_line):
        title = lines[i]
        poet_line = i + 1
    elif(i == poet_line):
        poet = lines[i][3:]
    else:
        poem_content.append(lines[i])

if(id != None): #最後一首詩
    poem = "".join(poem_content)
    s.append(f"INSERT INTO ts300 VALUES({id}, '{title}', '{poet}', '{poem}')")
    
for sql in s:
    cursor.execute(sql)

conn.commit()
conn.close()