from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://activity.books.com.tw/books66/"

html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html, "html.parser")

name_list = []
price_list = []

product_blocks = bsObj.findAll("div", {"class": "table-td"})
for item in product_blocks:
    name_tag = item.find("img")
    name = name_tag["alt"].strip() if name_tag and "alt" in name_tag.attrs else "無書名"
    name_list.append(name)
    price_block = item.find("ul", {"class": "price clearfix"})
    if price_block:
        price_tag = price_block.find("b", {"class": "text-style-01"})
        price = price_tag.text.strip() if price_tag else "無價格資訊"
    else:
        price = "無價格資訊"
    price_list.append(price)

start = 2
end = 8
filtered_names = name_list[start:end]
filtered_prices = price_list[start:end]

for i, (name, price) in enumerate(zip(filtered_names, filtered_prices), start=start + 1):
    print(f"{i-2}. {name} 特價 {price} 元")