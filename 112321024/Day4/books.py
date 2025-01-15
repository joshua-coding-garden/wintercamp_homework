from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://activity.books.com.tw/books66/"
html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html, "html.parser")

date = []
name = []
oringin = []
special = []

result = bsObj.findAll("div",{"class":"table-tr"})
for k in result[1].findAll("div",{"class":"table-td"}):
    date_rec = k.find("em",{"class":"date"})
    if date_rec:
        date.append(date_rec.get_text().strip())

    name_rec = k.find("h4")
    if name_rec:
        name.append(name_rec.get_text().strip())  

    oringin_rec = k.find("ul",{"class":"price clearfix"})
    if oringin_rec:
        oringin_price = oringin_rec.find_all("li")[0].get_text().strip()
        oringin.append(oringin_price)

    special_rec = k.find("ul",{"class":"price clearfix"})
    if special_rec:
        special_price = oringin_rec.find_all("li")[1].get_text().strip()
        special.append(special_price)


for i in range(min(len(date),len(name),len(oringin),len(special))):
    print(f"{date[i]} {name[i]} {oringin[i]} {special[i]}")