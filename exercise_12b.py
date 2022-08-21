import socket
import re

url = input('Enter url: ')
try:
    mepe = open(url)
except:
    print('Invalid url=', url)
    exit()

guo = mepe.read()
spt = guo.split('/')
host = spt[0]

my_sock = socket.socket(socket.AF_INET, socket.SOCK.STREAM)
my_sock.connect((host, 80))
dla = 'GET mepe HTTP/1.0\n\n'.encode()
my_sock.send(dla)

while True:
    data = my_sock.recv(3000)
    if (len(data)<1):break
    words = data.decode()
    cha = len(words)
    print('There are', cha, 'characters.')

my_scok.close()