from urllib.request import urlopen, Request
import urllib.parse
from bs4 import BeautifulSoup
import time

def getPhonetic(c):
    url = "https://ctext.org/dictionary.pl?if=gb&char='" + urllib.parse.quote(c) + "'"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}
    req = Request(url, headers=headers)
    html = urlopen(req).read().decode('utf-8')
    bsObj = BeautifulSoup(html, "html.parser")

    aList = []
    bList = bsObj.findAll("a", {"class": "noul"})
    for item in bList:
        ch = item.get_text()
        if '\u3105' <= ch <= '\u312f':
            aList.append(ch)
    return aList

for c in "高雄市":
    print(c, ','.join(getPhonetic(c)))
    time.sleep(1)