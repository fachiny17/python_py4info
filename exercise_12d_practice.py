import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

url = input('Enter url: ')
soup = BeautifulSoup(urllib.request.urlopen(html).read(), 'html.parser')

counts = 0
tags = soup('p')
for tag in tags:
    counts = counts + tag

print('There are', counts, 'paragraphs.') 