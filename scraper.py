from bs4 import BeautifulSoup
import urllib.request
import bs4
import requests
import re
import gspread
import json
import time
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import sys #parameters are [# of rows down to log]


def trumpscrape():
    page = requests.get("http://rss.cnn.com/rss/cnn_topstories.rss")
    data = page.text
    soup = BeautifulSoup(data, 'lxml')
    y = 0
    a = soup.find_all("description")
    Trumps = 0
    c = re.compile('(?:^|\W)Trump(?:$|\W)')
    for y in range(len(soup.find_all("description"))):
        tempray = []
        debugarray = []
        i = 0
        whilebool = True
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
    return Trumps

def Update_Sheet(iteration_num, numtrumps):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("CnnScraper").sheet1
    sheet.update_cell(iteration_num,1,numtrumps)
    sheet.update_cell(iteration_num,2,str(datetime.now()))
    str(datetime.now())



if __name__ == '__main__':
    iterations = 1
    while True:
        numtrump = trumpscrape()
        Update_Sheet(iterations, numtrump)
        iterations += 1
        time.sleep(3600)


