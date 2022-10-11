
from datetime import datetime


class Reserve:
    def __init__(self, resNum: int = 0, resdate: datetime = None, id: str = None, rtNm: str = None,
                 plainNo: str = None, stNm: str = None, stNmD: str = None, reserve: str = None, etc: str = None):
        self.resNum = resNum
        self.resdate = resdate
        self.id = id
        self.rtNm = rtNm  # 노선명
        self.plainNo = plainNo # 차량 번호
        self.stNm = stNm # 승차 정류소명
        self.stNmD = stNmD # 하차정류소명
        self.reserve = reserve # 예약 확인
        self.etc = etc  # 예약 취소 사유


    def __str__(self): #toString()
        return 'resNum :'+self.resNum+ '/ '+ 'resdate :'+self.resdate+ '/ '+'id :'+self.id+' / '\
               + 'rtNm :' +self.rtNm+ ' / '\
               +'plainNo :' +self.plainNo+ ' / '+ 'stNm :' +self.stNm+ ' / ' + 'stNmD :' +self.stNmD+ ' / '\
               +'reserve :' +self.reserve+ ' / ' +'etc :' +self.etc