import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

trt = input('Enter url: ')
mop = urllib.request.urlopen(trt, context=ctx).read()
soup = BeautifulSoup(mop, 'html.parser')
lst = list()
tags = soup('span')
for tag in tags:
    lst.apend(int(tag.contents[0]))
print(sum(lst))