from reservation.vo import Reserve
from reservation.dao import ReserveDao


class ReService:
    def __init__(self):
        self.dao = ReserveDao()

    # 추가
    def addReserve(self, r:Reserve):
        self.dao.insert(r)

    def getById(self, id:str)->Reserve: #타입 힌트
        return self.dao.selectById(id)

    # 삭제
    def delReserve(self, id:str):
        self.dao.delete(id)

    def editReserve(self, r:Reserve):
        self.dao.update(r)