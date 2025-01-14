from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://web.ee.ntu.edu.tw/teacher_index_all.php'
html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html, "html.parser")

name = bsObj.findAll("td", {"class":"teacher_list_title"})
email = bsObj.select("a > img[src *= 'program/email_image.php']")
group = bsObj.findAll("td", {"class": "teacher_list_title2"}, string=lambda x: x and "組別：" in x)
for i, (n, e, g) in enumerate(zip(name, email, group), start=1):
    t = g.get_text().strip()
    print(i, n.get_text().strip(), e.get("alt"), t.replace("組別：", ""))
