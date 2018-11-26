from bs4 import BeautifulSoup
import urllib.request
import bs4
import requests


page = requests.get("http://rss.cnn.com/rss/cnn_topstories.rss")
data = page.text

soup = BeautifulSoup(data, 'lxml')
print(soup.prettify())
print(soup.find_all("a",class_="banner-text screaming-banner-text banner-text-size--char-44"))
print(soup.find_all("a",href=True))
print(soup.find_all("h4", class_="itemtitle"))
for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])

y = 0
a = soup.find_all("description")
for y in range(len(soup.find_all("description"))):
    print(a[y])
    print("\n")
    tempray = []
    i = 0
    whilebool = True
    str(a)
    while whilebool:
        i += 1
        if a[i] == ">":
            i +=1
            isdone = False
            while not isdone :
                if (a[i] == "." and a[i+1] == "&" and [i+2] == "l" and  a[i+3] == "t" and  a[i+1] == ";"):
                    isdone = True
                    whilebool = False
                else:
                    tempray.append(a[i])

    print(tempray)
    y += 1





