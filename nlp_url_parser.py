import urllib.request
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,} 
url="http://news.stanford.edu/2005/06/14/jobs-061505/"

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read()

for i in bs(data).find_all('p'):
    print(i.get_text())
