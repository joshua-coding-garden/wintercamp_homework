from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://web.ee.ntu.edu.tw/teacher_index_all.php'
html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html,"html.parser")

name = []
email = []
part = []

name_rec = bsObj.findAll("td",{"class":"teacher_list_title"})
email_rec = bsObj.findAll("td",{"class":"teacher_list"})
part_rec = bsObj.findAll("td",{"class":"teacher_list_title2"})

for item_1 in name_rec:
    result_1 =  item_1.find("a").get_text()
    name.append(result_1)
for item_2 in email_rec:
    result_2 =  item_2.find("img")["alt"]
    email.append(result_2)
for item_3 in part_rec:
    result_3 =  item_3.get_text()
    # 沒有這行判斷會連其他(title2)資料一起抓到
    if result_3.startswith("組別："):
        result_3_1 = result_3.replace("組別：","")
        part.append(result_3_1)
for item_4 in range(min(len(name),len(email),len(part))):
    print(f"{item_4 + 1}. {name[item_4]} {email[item_4]} {part[item_4]}")