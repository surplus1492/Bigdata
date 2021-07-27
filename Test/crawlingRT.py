import os
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

response = req.get('https://issue.zum.com/')

dom = bs(response.text, 'html.parser')
divs = dom.select('#issueKeywordList > li > div.cont')

dir = '/home/bigdata/Test/RT_T/{:%Y-%m-%d}'.format(datetime.now())

if not os.path.exists(dir):
    os.makedirs(dir)

fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')

for div in divs:
    rank = div.find(class_='num').text
    word = div.find(class_='word').text
    file.write('%s : %s\n' %(rank[:-1], word))

file.close()
