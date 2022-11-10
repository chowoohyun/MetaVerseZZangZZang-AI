from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo


client = pymongo.MongoClient(
    "mongodb+srv://metaverse123:hongil123@accidentlyunity.ts7ta4j.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.zzang


# 사용할 DB 테이블 (컬렉션)
# 회의 정보 DB
meetingDB = db.meeting
# STT 내용 저장
talkDB = db.talk
# 키워드
keywordDB = db.keyword
# google 결과
searchDB = db.search
# google 이미지 저장
imageDB = db.image
# 요약
summaryDB = db.summary
# 네트워크 그래프 저장
graphDB = db.graph
# 네트워크 그래프 노드, 엣지 저장
networkxDB = db.networkx

print(meetingDB)
