from bs4 import BeautifulSoup
import urllib.request
import bs4
import requests
import re
c = re.compile('(?:^|\W)Trump(?:$|\W)')


page = requests.get("http://rss.cnn.com/rss/cnn_topstories.rss")
data = page.text

soup = BeautifulSoup(data, 'lxml')


Trumps = 0
y = 0
a = soup.find_all("description")
for y in range(len(soup.find_all("description"))):
    tempray = []
    debugarray = []
    i = 0
    whilebool = True
    str(a)
    sublist = a[y]
    teststring = sublist.text
    for i in range(len(teststring)):
        character = sublist.text[i]
        if character == "<":
            break
        tempray.append(teststring[i])
        i += 1
    if len(tempray) >= 1:
        tempray.append("\n")
    Trumps += len(c.findall(''.join(tempray)))
    y += 1

print(Trumps)                                   #number of trumps!



