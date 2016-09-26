import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import urllib.request
from bs4 import BeautifulSoup as bs
from nltk.tokenize import RegexpTokenizer
import json

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,} 
url="http://news.stanford.edu/2005/06/14/jobs-061505/"

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read()

example_sentence = ""

for i in bs(data).find_all('p'):
    example_sentence += (i.get_text() + " ")



# Tutorial from sentdex -> https://www.youtube.com/playlist?list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL


#English stop words already defined by nltk
stop_words = set(stopwords.words("english"))

tokenizer = RegexpTokenizer(r'\w+')

example_sentence = tokenizer.tokenize(example_sentence)


filtered_sentence = []

for w in example_sentence:
	if w not in stop_words:
		filtered_sentence.append(w)


filtered_sentence.sort()

# print(filtered_sentence)

frequency_count_sentence = {}

for w in filtered_sentence:
	if w in frequency_count_sentence:
		frequency_count_sentence[w] += 10
	else:
		frequency_count_sentence[w] = 10


# print(json.dumps(frequency_count_sentence))

# print( frequency_count_sentence)

json_object = []

for word in frequency_count_sentence:
	obj2 = {}
	obj2["text"] = word
	obj2["size"] = frequency_count_sentence[word]
	json_object.append(obj2)

print(json.dumps(json_object))