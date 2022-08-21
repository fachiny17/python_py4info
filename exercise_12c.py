import urllib.request, urllib.parse, urllib.error

tol = ('Enter url: ')
mepe = urllib.request.urlopen(tol)

for line in mepe:
    words = line.decode().split()
    if (len(words)>3000):continue
    print(words)
    print(len(words))