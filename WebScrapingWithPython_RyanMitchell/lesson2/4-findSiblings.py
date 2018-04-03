from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read())

for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)