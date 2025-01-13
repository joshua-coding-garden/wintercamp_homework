from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import urllib.parse
import time
import os

file = "phonetic.tab"

def load_cache():
    cache = {}
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(" ", 1)
                if len(parts) == 2:
                    cache[parts[0]] = parts[1]
    return cache

def save_to_cache(c, phonetics):
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{c} {' '.join(phonetics)}\n")

def getPhonetic(c, cache):
    if c in cache:
        return cache[c].split(",")
    url = "https://ctext.org/dictionary.pl?if=gb&char='" + urllib.parse.quote(c) + "'"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}
    req = Request(url, headers=headers)
    html = urlopen(req).read().decode("utf-8")
    bsObj = BeautifulSoup(html, "html.parser")

    aList = []
    bList = bsObj.findAll("a", {"class": "noul"})
    for item in bList:
        ch = item.get_text()
        if '\u3105' <= ch <= '\u312f':
            aList.append(ch)

    if aList:
        save_to_cache(c, aList)
        cache[c] = ",".join(aList)

    return aList

def main():
    cache = load_cache()
    user_input = input("請輸入要查詢的中文字: ")

    for c in user_input:
        phonetics = getPhonetic(c, cache)
        print(c, ','.join(phonetics))
        time.sleep(1)

if __name__ == "__main__":
    main()