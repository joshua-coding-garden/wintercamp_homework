from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://activity.books.com.tw/books66/'
html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html, "html.parser")

date = bsObj.findAll("em", {"class":"date"})
name = bsObj.select("h4 > a[href *= 'books66_title']")
price = bsObj.findAll("b", {"class":"text-style-01"})

for i, (d, n, p) in enumerate(zip(date, name, price), start=1):
    print("{}. {}\n   書名:{}\n   66折優惠價:{}元".format(i, d.get_text().strip(), n.get_text().strip(), p.get_text().strip()))