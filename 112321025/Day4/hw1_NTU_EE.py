from urllib.request import urlopen 
from bs4 import BeautifulSoup

url = 'https://web.ee.ntu.edu.tw/teacher_index_all.php'
html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html, "html.parser")
aList = bsObj.findAll("td", {"class": "teacher_list_title"})
bList = bsObj.findAll("td", {"class": "teacher_list"})
cList = bsObj.findAll("td", string=lambda text: text and "組別：" in text)
index = 1
for a, b, c in zip(aList, bList, cList):
    name = a.get_text()
    email = b.img["alt"].strip()
    group = c.get_text(strip=True).replace("組別：", "")
    print(index, name, email, group)
    index += 1