"""
2021/06/08
김영현
실시간 검색어 크롤링 실습
"""

import os
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

# 페이지 요청하기
response = req.get('https://issue.zum.com/')
# print(response.text)

# 페이지 파싱하기
dom = bs(response.text, 'html.parser')
divs = dom.select('#issueKeywordList > li > div.cont')

# 디렉터리 생성
dir = './keyword/{:%Y-%m-%d}'.format(datetime.now())

if not os.path.exists(dir):
    os.makedirs(dir)

# 파일 생성
fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')

# 파일 저장
for div in divs:
    rank = div.find(class_='num').text
    word = div.find(class_='word').text
    file.write('%s,%s\n' %(rank[:-1], word))

file.close()

print('검색어 수집 완료...')