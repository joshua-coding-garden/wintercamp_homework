import sqlite3
db_filename = 'test.db'
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

with open("ts300.txt","r",encoding = "utf-8") as file:
    lines = file.readlines()

id = ""
title = ""
poet = ""
poem = ""
result = []
have_number = []

for line in lines:
    line = line.strip()
    if not line:
        if id and title and poet and poem:
            result.append((id,title,poet,poem))
            id = ""
            title = ""
            poet = ""
            poem = ""
    elif not id:
        id = line
    elif not title:
        title = line
    elif not poet:
        if line[0] != '作':
            title += line
        else:
            poet = line.replace("作者","")
    else:
        poem += line
        if any(char.isnumeric() for char in line):
            have_number.append(line)

if id and title and poet and poem:
    result.append((id,title,poet,poem))

for i in result:
    id,title,poet,poem = i
    sql = f"INSERT INTO ts300 VALUES('{id}','{title}','{poet}','{poem}')"
    cursor.execute(sql)

for j in have_number:
    print(j)

conn.commit()
cursor.close()
conn.close()