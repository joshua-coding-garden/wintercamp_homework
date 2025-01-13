from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://web.ee.ntu.edu.tw/teacher_index_all.php'
html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html, "html.parser")

name = bsObj.findAll("td", {"class":"teacher_list_title"})
email = bsObj.findAll("a", {"style":"position:absolute; cursor:default;"})
group = bsObj.findAll("td", {"class": "teacher_list_title2"}, string=lambda x: x and "組別：" in x)

for i, (n, e, g) in enumerate(zip(name, email, group), start=1):
    img = e.find("img")
    t = g.get_text().strip()
    print(i, n.get_text().strip(), img.get("alt"), t.replace("組別：", ""))