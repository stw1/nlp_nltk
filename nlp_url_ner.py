# Named Entity Recognition with NLTK

# NE Type and Examples
# ORGANIZATION - Georgia-Pacific Corp., WHO
# PERSON - Eddy Bonte, President Obama
# LOCATION - Murray River, Mount Everest
# DATE - June, 2008-06-29
# TIME - two fifty a m, 1:30 p.m.
# MONEY - 175 million Canadian Dollars, GBP 10.40
# PERCENT - twenty pct, 18.75 %
# FACILITY - Washington Monument, Stonehenge
# GPE - South East Asia, Midlothian

import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
import urllib.request
from bs4 import BeautifulSoup as bs
from nltk.tokenize import RegexpTokenizer

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,} 
url="http://news.stanford.edu/2005/06/14/jobs-061505/"

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read()

example_sentence = ""

for i in bs(data).find_all('p'):
    example_sentence += (i.get_text() + " ")


# print(example_sentence)

tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
tokenized = tokenizer.tokenize(example_sentence)



def process_content():
    try:
        for i in tokenized[1:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt = nltk.ne_chunk(tagged)
            print(namedEnt)
    except Exception as e:
        print(str(e))


process_content()