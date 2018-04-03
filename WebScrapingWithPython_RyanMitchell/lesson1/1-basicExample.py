from urllib.request import urlopen
from bs4 import BeautifulSoup
#Retrieve HTML string from the URL
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())
