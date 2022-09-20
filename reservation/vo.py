class Reserve:
    def __init__(self, reservenum: int = 0, id: str = None, arrmsg: str = None, plainNo: str = None,
                stNm: str = None, stNmD: str = None, reserve: str = None, etc: str = None):
        self.reservenum = reservenum
        self.id = id
        self.arrmsg = arrmsg
        self.plainNo = plainNo
        self.stNm = stNm
        self.stNmD = stNmD
        self.reserve = reserve
        self.etc = etc


    def __str__(self): #toString()
        return 'id :'+self.id+' / '+'arrmsg : '+self.arrmsg+' / '+ ' plainNo :' + self.plainNo + ' / '\
               + 'stNm :' + self.stNm+ ' / ' + 'stNmD :' + self.stNmD+ ' / ' 'reserve :' + self.reserve+ ' / ' \
               +'etc :' + self.etc