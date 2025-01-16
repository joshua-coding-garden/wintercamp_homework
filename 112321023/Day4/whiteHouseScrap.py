from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://www.whitehouse.gov/'
html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html, "html.parser")
titles = bsObj.findAll('h3')

for i in range(len(titles)): 
    print(i + 1, titles[i].get_text().strip())