import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
hat = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(hat, 'html.parser')

counts = 0
for para in soup.find_all("p"):
    counts = counts + para
print('There are', counts, 'paragraphs.')