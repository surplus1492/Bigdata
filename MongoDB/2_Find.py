from pymongo import MongoClient as mongo
from datetime import datetime

# 1단계 - mongodb 접속
conn = mongo('mongodb://admin:1234@192.168.100.102:27017')

# 2단계 - DB 선택
db = conn.get_database('test')

# 3단계 - Collection 선택
collection = db.get_collection('MEMBER')

# 4단계 - 쿼리 실행
rs = collection.find()

for row in rs:
    print('---------------------------')
    print('%s, %s' % (row['uid'], row['name']))

# 5단계 - mongodb 종료
conn.close()