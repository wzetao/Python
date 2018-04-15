from urllib.request import urlopen
from io import StringIO
import csv

#data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read()
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
for row in csvReader:
    print(row)