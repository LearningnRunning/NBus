class Reserve:
    def __init__(self, reservenum: int = 0, id: str = None, arrmsg: str = None, rtNm: str = None,
                 plainNo: str = None, stNm: str = None, stNmD: str = None, reserve: str = None, etc: str = None):
        self.reservenum = reservenum
        self.id = id
        self.arrmsg = arrmsg  # 도착예정시간
        self.rtNm = rtNm  # 노선 번호
        self.plainNo = plainNo # 차량 번호
        self.stNm = stNm # 승차 정류소명
        self.stNmD = stNmD # 하차정류소명
        self.reserve = reserve # 예약 확인
        self.etc = etc  # 예약 취소 사유


    def __str__(self): #toString()
        return 'reservenum :'+self.reservenum+' / '+'id :'+self.id+' / '+'arrmsg : '+self.arrmsg+' / '+ ' rtNm :' +self.rtNm+ ' / '\
               +' plainNo :' +self.plainNo+ ' / '+ 'stNm :' +self.stNm+ ' / ' + 'stNmD :' +self.stNmD+ ' / '\
               +'reserve :' +self.reserve+ ' / ' +'etc :' +self.etc