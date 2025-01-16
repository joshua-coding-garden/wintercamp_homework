from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://poet.ncnu.org/page1.html"
html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.h1)