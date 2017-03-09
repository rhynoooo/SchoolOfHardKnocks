import sys
import requests
from BeautifulSoup import BeautifulSoup

try:
	response = requests.get('http://www.nbcnews.com/specials/geographyofpoverty-heartland-1')
except:
	print("connection couldn't be established")
	sys.exit(1)

if (response.status_code == 200):
	print("Successful: http call")
else:
	print("Error: Status Code %s" % str(response.status_code))
	sys.exit(1)

content = response.content
soup = BeautifulSoup(content)
p_tags = soup.findAll('p')

words = {}

for p in p_tags:
	word_list = p.text.split(' ')
	for word in word_list:
		try:
			words[word] += 1
		except:
			words[word] = 1

numbers = {}

for x in words:
	try:
		numbers[words[x]].append(x)
	except:
		numbers[words[x]] = list(x)

print(numbers.values())