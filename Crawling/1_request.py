"""
2021/06/07
김영현
웹 Request 실습
"""
import requests as req

# 네이버 페이지 요청
response = req.get('http://naver.com')
print(response)  # response [200] -> 요청이 성공했음을 나타냄
print(response.text)
