# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# url = 'https://www.englishclub.com/ref/idiom-of-the-day.php'
# html = urlopen(url).read().decode()
# bsObj = BeautifulSoup(html, "html.parser")
# idiom = bsObj.find("h2", {"class": "clr-green"}).get_text()
# print( idiom )

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
url = 'https://www.englishclub.com/ref/idiom-of-the-day.php'
req = Request(url, headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_9_3) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/35.0.1916.47 Safari/537.36'} )
html = urlopen(req).read().decode()
bsObj = BeautifulSoup(html, "html.parser")
idiom = bsObj.find("h2", {"class": "clr-green"}).get_text()
print( idiom )