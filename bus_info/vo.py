class Bus:
    def __init__(self, busid=None, busnm=None, ststat=None, edstat=None,
                 sttime=None, edtime=None, term=None):
        self.busid = busid
        self.busnm = busnm
        self.ststat = ststat
        self.edstat = edstat
        self.sttime = sttime
        self.edtime = edtime
        self.term = term

    def __str__(self):
        s = ''
        s += '버스id: '+self.busid + '\n'
        s += '버스번호: ' + self.busnm + '\n'
        s += '기점: ' + self.ststat + '\n'
        s += '종점: ' + self.edstat + '\n'
        s += '첫차시간: ' + self.sttime + '\n'
        s += '막차시간: ' + self.edtime + '\n'
        s += '배차간격: ' + self.term + '\n'
        return s

class Station:
    def __init__(self, seq=None, name=None, direction=None, x=None, y=None, arsId=None):
        self.seq = seq
        self.name = name
        self.direction = direction
        self.x = x
        self.y = y
        self.arsId = arsId

