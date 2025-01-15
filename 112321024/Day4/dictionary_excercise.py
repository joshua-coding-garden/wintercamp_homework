from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time
import urllib.parse

headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}

def getPhonetic(c):
    url = "https://ctext.org/dictionary.pl?if=gb&char='" + urllib.parse.quote(c) + "'"
    req = Request(url,  headers=headers)
    html = urlopen(req).read().decode('utf-8')
    bsObj = BeautifulSoup(html, "html.parser")

    aList = []
    result = bsObj.findAll("a",{"class":"noul"})
    for i in result:
        item = i.get_text()
        if '\u3105' <= item <= '\u312f':
            aList.append(item)
    return aList

for c in "高雄市":
    print(c, ','.join(getPhonetic(c)))
    time.sleep(1)