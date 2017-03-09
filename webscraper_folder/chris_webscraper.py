import sys
import re
import requests
from BeautifulSoup import BeautifulSoup

def http_call(url):
	"This makes an html call to nbc"
	try:
		response = requests.get(url)
	except:
		print("connection couldn't be established")
		sys.exit(1)

	if (response.status_code == 200):
		print("Successful: http call")
	else:
		print("Error: Status Code %s" % str(response.status_code))
		sys.exit(1)	
	return response

def html_parse(response):
	"This is a html parser for nbc"
	content = response.content
	soup = BeautifulSoup(content)
	p_tags = soup.findAll('p')
	return p_tags

def word_by_number_dict(p_tags):
	"This takes parsed html and returns words by count"
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
	return words

def number_by_word_list(words):
	"this finds all the counts and pairs words as a list with them"
	numbers = {}

	for x in words:
		if numbers.has_key(words[x]):
			numbers[words[x]].append(x)
		else:
			numbers[words[x]] = [x]
	return numbers

def top_report(numbers):
	" This is a top 20 report"
	top5 = sorted(numbers.keys())
	top5.reverse()

	print
	print "the most common words report:"
	print

	i = 1
	print('rank\tcount\twords')
	for x in top5[0:10]:
		tup = [str(i), str(x), ', '.join(numbers[x]).encode('ascii')]
		print('\t'.join(tup))
		i += 1
	print
	return 0

def web_scrape(url):
	response = http_call(url)
	p_tags = html_parse(response)
	words = word_by_number_dict(p_tags)
	numbers = number_by_word_list(words)
	top_report(numbers)
	return 0


def main():
	" main function"
	urls=[ 
			'http://www.msnbc.com/interactives/geography-of-poverty/index.html',
			'http://www.msnbc.com/interactives/geography-of-poverty/sw.html',
			'http://www.msnbc.com/interactives/geography-of-poverty/se.html',
			'http://www.msnbc.com/interactives/geography-of-poverty/ne.html',
			'http://www.msnbc.com/interactives/geography-of-poverty/nw.html',
			'http://www.nbcnews.com/specials/geographyofpoverty-heartland-1',
			'http://www.nbcnews.com/specials/geographyofpoverty-big-city'
			]

	print("scraping the following urls:")
	for url in urls:
		print url

	print 

	for url in urls:
		web_scrape(url)
	print("finished scraping...")
	return 0

main()

