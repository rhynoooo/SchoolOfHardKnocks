import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.nbcnews.com/specials/geographyofpoverty-heartland-1.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
caption = soup.find('figcaption')

#for row in table.findAll('tr'):
print soup.prettify() 
