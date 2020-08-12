import requests
import re
from bs4 import BeautifulSoup
r=requests.get('https://python123.io/ws/demo.html')
# print(r.text)
demo= r.text
soup=BeautifulSoup(demo,"html.parser")
# print(soup.prettify())
# print(soup.a.parent.name)
# print(soup.a.attrs['class'])
# print(soup.a.string)
# print(soup.a.next_sibling.next_sibling)
for tag in soup(re.compile('b')):
    print(tag.name)