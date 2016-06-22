import urllib2
import pprint
import operator
from bs4 import BeautifulSoup

url = 'https://www.mapbox.com/about/team/'
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

results = soup.find_all("h4", class_="quiet")
employee_count = 0
positions = []
positionCount = {}

for result in results:
	employee_count += 1
	if result.string.upper() in positions:
		count = positionCount[result.string.upper()]+1
		positionCount[result.string.upper()]=count
	else:
		positions.append(result.string.upper())
		positionCount[result.string.upper()]=1
#	print result.string

pprint.pprint(sorted(positionCount.items(), key=operator.itemgetter(1), reverse=True));
print(employee_count)
