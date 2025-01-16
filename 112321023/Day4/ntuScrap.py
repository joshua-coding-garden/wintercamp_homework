from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://web.ee.ntu.edu.tw/teacher_index_all.php"

html = urlopen(url).read().decode()
bsObj = BeautifulSoup(html, "html.parser")

names = bsObj.findAll('td', {'class':'teacher_list_title'})
email_img = bsObj.select('img[src*="program/email_image.php"]')
#emails = [img['alt'] for img in email_img]
groups = bsObj.findAll('td', {'class':'teacher_list_title2'}, string=re.compile('^組別'))
for i in range(len(names)):
    print(i+1, names[i].get_text(), email_img[i].get('alt'), groups[i].get_text()[3:])