from urllib.request import urlopen 
from bs4 import BeautifulSoup

url = 'https://activity.books.com.tw/books66/'
html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html, "html.parser")
title = bsObj.find("h3", {"class" : "title"}).get_text()
dateList = bsObj.findAll("em", {"class" : "date"})
nameList = bsObj.findAll("h4")
priceList = bsObj.findAll("ul", {"class" : "price clearfix"})
index = 1
print(title)
for d, n, p in zip(dateList, nameList, priceList):
    date = d.get_text()
    name = n.get_text()
    price = p.b.get_text()
    print(index, ".", date)
    print("    書名:", name)
    print("    66折優惠價:", price, "元")
    index += 1