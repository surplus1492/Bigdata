from pymongo import MongoClient as mongo
from datetime import datetime

# 1단계 - mongodb 접속
conn = mongo('mongodb://admin:1234@192.168.100.102:27017')

# 2단계 - DB 선택
db = conn.get_database('test')

# 3단계 - Collection 선택
collection = db.get_collection('MEMBER')

# 4단계 - 쿼리 실행
collection.insert_one({'uid': 'a101', 'name': '김유신', 'hp': '010-1212-1010'})
collection.insert_one({'uid': 'a102', 'name': '김춘추', 'hp': '010-1212-1011', 'pos': '대리', 'dep': 101, 'rdate': datetime.now()})
collection.insert_one({'uid': 'a103',
                       'name': '장보고',
                       'hp': '010-1212-1011',
                       'pos': '대리',
                       'dep': 101,
                       'rdate': datetime.now()})

# 5단계 - MongoDB 종료
conn.close()

print('Insert 완료...')
