import string
import codecs
from tabulate import tabulate
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import requests
from BeautifulSoup import BeautifulSoup
from collections import Counter
from stop_words import get_stop_words

#Here I pull the website's HTML
url = 'http://www.nbcnews.com/specials/geographyofpoverty-heartland-1'
response = requests.get(url)
html = response.content


soup = BeautifulSoup(html)
lst = []

#here I am finding all of the contents with the paragraph HTML codes
for p in soup.findAll('p'):
    para = str(p.text.encode('utf-8'))
 #using list comprehension I remove anything nonalphanumeric
 #and split it into separate individual strings.
    para_f = "".join([e.lower() for e in para if e in string.letters or e in string.whitespace]).split()
    lst = lst + para_f
#Here I pull stop words
stop_words = get_stop_words('english')

new_lst = []
#Here I filter the data by only adding the words to the new list if they 
#are not part of the list of stop words
for ele in lst:
    if ele not in stop_words:
        new_lst.append(ele)

#Here is a quick method of using Counter to identify the most common words
#c = Counter(new_lst).most_common(20)
#print c 

### Here I am counting all the words 
###and inserting them into a dictionary where the distinctive words are the key 
###and the frequency of the word as its value 
dict1 = {}

for word in new_lst:
	if word in dict1:
		dict1[word] = new_lst.count(word) + 1
	else:
		dict1[word] = 1
#print dict1

print "Successful: http call"
print "The most common words report:"



data =sorted(zip(dict1.values(), dict1.keys()), reverse = True)[:50]
data2 ={}

#Here I am grouping the words based upon the word's frequency. 
#I begin by looping through the data dictionary where I had previously 
#identified the frequency of each word. If the key(frequency of the word) 
#has the same frequency of any other word then I append that word to the list
#in the value position of the dictionary type data structure. Basically it is 
#grouping all of the words with the same frequency of occurrence as a list in a 
#dictionary data structure. If that frequency of the word has not been identified
#yet in the new dictionary called data2 then it stores the frequency of the word 
#as the dictionary's key and creates a new empty list and places that in the value 
#position. Then it appends that word to that empty list in the dictionary.  
for key, value in data:
	if key in data2:
		data2[key].append(value)
	else:
		data2[key] = []
		data2[key].append(value)
print data2

# this reverse sorts and slices the data for how 
#many most common words I desire to find
data3 =sorted(zip(data2.keys(), data2.values()), reverse = True)[:50]

#this places the data in a table format
print tabulate(data3, headers = ['Count','Words'])







    
 
    







    


