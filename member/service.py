from member.vo import Member
from member.dao import MemberDao


class MemberService:
    def __init__(self):
        self.dao = MemberDao()

    # 추가
    def addMember(self, m:Member):
        self.dao.insert(m)

    def getById(self, id:str)->Member:
        return self.dao.select(id)

    # 삭제
    def delMember(self, id:str):
        self.dao.delete(id)

    def editMember(self, m:Member):
        self.dao.update(m)
