import os
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time
import urllib.parse

headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}

PHONETIC_FILE = "phonetic.tab"

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

def load_phonetic_file():
    phonetic_dict = {}
    if os.path.exists(PHONETIC_FILE):
        with open(PHONETIC_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    char,phonetics = line.split(maxsplit = 1)
                    phonetic_dict[char] = phonetics
    return phonetic_dict

def save_to_phonetic_file(c,aList):
    with open(PHONETIC_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{c} {aList}\n")

def get_phonetic(c,phonetic_dict):
    if c in phonetic_dict:
        return phonetic_dict[c]
    else:
        phonetics = getPhonetic(c)
        if phonetics:
            phonetic_dict[c] = phonetics
            save_to_phonetic_file(c, phonetics)
    return phonetics

if __name__ == "__main__":
    phonetic_dict = load_phonetic_file()
    test_string = input("")
    for c in test_string:
        phonetics = get_phonetic(c, phonetic_dict)
        if phonetics:
            print(f"{c}: {phonetics}")    