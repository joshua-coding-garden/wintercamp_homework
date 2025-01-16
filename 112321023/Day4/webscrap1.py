# Retrieve HTML string from a URL
from urllib.request import urlopen
url = "http://poet.ncnu.org/page1.html" # Universal Resource Locator
data = urlopen(url).read()
html = data.decode()
print(html)