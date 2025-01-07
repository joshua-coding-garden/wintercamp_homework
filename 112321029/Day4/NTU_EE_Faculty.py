from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://web.ee.ntu.edu.tw/teacher_index_all.php"

html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html, "html.parser")

name_list = []
email_list = []
main_list = []

nameResult = bsObj.findAll("td", {"class": "teacher_list_title"})
for item in nameResult:
    name = item.find("a").get_text().strip()
    name_list.append(name)

emailResult = bsObj.findAll("td", {"class": "teacher_list"})
for eitem in emailResult:
    email = eitem.find("img")["alt"].strip()
    email_list.append(email)

mainResult = bsObj.findAll("td", {"class": "teacher_list_title2"})
for mitem in mainResult:
    main = mitem.get_text().strip()
    if main.startswith("組別："):
        main_cleaned = main.replace("組別：", "").strip()
        main_list.append(main_cleaned)

for i in range(max(len(name_list), len(email_list), len(main_list))):
    name = name_list[i]
    email = email_list[i]
    main = main_list[i]
    print(f"{i}. {name} {email} {main}")
