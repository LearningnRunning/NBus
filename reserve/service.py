from datetime import datetime

from reserve.vo import Reserve
from reserve.dao import ReserveDao

class ResService:
    def __init__(self):
        self.dao = ReserveDao()

    # 추가
    def addReserve(self, r:Reserve):
        self.dao.insert(r)

    # 내 예약 정보 검색
    def getById(self, id:str)->Reserve:
        return self.dao.select(id) # select를 변경

    # 날짜 기준 검색
    def getByDate(self, id:str)->Reserve:
        return self.dao.selectbyDate(id)

    def getByDatePast(self, id:str)->Reserve:
        return self.dao.selectbyDatepast(id)


    # 삭제
    def delReserve(self, reservenum): # 예약번호로 취소
        self.dao.delete(reservenum)

    def editReserve(self, r:Reserve):
        self.dao.update(r)