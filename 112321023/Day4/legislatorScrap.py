from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.ly.gov.tw/Pages/List.aspx?nodeid=109'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Accept': \
'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/ webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}

req = Request(url, headers=headers)
html = urlopen(req).read().decode()
bsObj = BeautifulSoup(html, "html.parser")

a = bsObj.findAll("a", {"data-toggle":"tooltip"})
party = bsObj.findAll("img", {"class":"six-party-icon"})
name = bsObj.findAll("div", {"class":"legislatorname"})

diff_party = set()

for i in range(len(name)):
    diff_party.add(party[i].get('alt')[:-2])
    print(party[i].get('alt').replace('徽章', ''), name[i].get_text())

print( "Legislator Total:", len(a) )
print( "Party List:", diff_party)