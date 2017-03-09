import sys
import re
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
		regex = re.compile('[^a-zA-Z]')
		word = regex.sub('', word).lower()
		if word.strip() == '' or len(word.strip()) == 1:
			continue
		try:
			if word == 'h':
				print "h!"
			words[word] += 1
		except:
			words[word] = 1

numbers = {}

for x in words:
	if numbers.has_key(words[x]):
		numbers[words[x]].append(x)
	else:
		numbers[words[x]] = [x]

top5 = sorted(numbers.keys())
top5.reverse()

print
print "the most common words report:"
print

i = 1
print('rank\tcount\twords')
for x in top5[0:20]:
	tup = [str(i), str(x), ', '.join(numbers[x]).encode('ascii')]
	print('\t'.join(tup))
	i += 1
print
