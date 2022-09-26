from reserve.vo import Reserve
from reserve.dao import ReserveDao

class ResService:
    def __init__(self):
        self.dao = ReserveDao()

    # 추가
    def addReserve(self, r:Reserve):
        self.dao.insert(r)

    def getById(self, id:str)->Reserve: #타입 힌트
        return self.dao.select(id)

    # 삭제
    def delReserve(self, id:str):
        self.dao.delete(id)

    def editReserve(self, r:Reserve):
        self.dao.update(r)