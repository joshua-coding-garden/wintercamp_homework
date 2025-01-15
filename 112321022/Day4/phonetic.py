from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib.parse import quote
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}
f = "phonetic.tab"

def load():
    data = {}
    infile = open(f, "r", encoding="utf-8")
    for line in infile:
        line = line.strip().split(" ", 1)
        data[line[0]] = line[1]
    infile.close()
    return data

def getPhonetic(c):
    url = "https://ctext.org/dictionary.pl?if=gb&char='" + quote(c) + "'"
    req = Request(url,  headers=headers)
    html = urlopen(req).read().decode()
    bsObj = BeautifulSoup(html, "html.parser")

    aList = []
    ch = bsObj.findAll("a", {"class":"noul", "style":"white-space: nowrap;"})
    for i in ch:
        i = i.get_text().strip()
        if '\u3105' <= i <= '\u312f':
            aList.append(i)
    aList = ','.join(aList)

    apfile = open(f, "a", encoding="utf-8")
    print(c + ' ' + aList, file=apfile)
    apfile.close()

    return aList

if __name__ == "__main__":
    while True:
        try:
            s = load()
            i = input("input:")
            if i in s:
                print(s[i])
            else:
                phonetics = getPhonetic(i)
                print(phonetics)
                time.sleep(1)
        except EOFError:
            break