class Bus1:
    def __init__(self, arsId=None, stNm=None):
        self.arsId = arsId # 정류소 id
        self.stNm = stNm

    def __str__(self):
        s = ''
        s += '정류소고유번호' + self.arsId + '\n'  # 확인 필요
        s += '정류소명' + self.stNm + '\n'

        return s


class Bus2:
    def __init__(self,  paramId1=None, paramId2=None, busRouteId=None, stNm=None,rtNm=None, firstTm=None,lastTm=None, term=None,
                 vehId1=None,plainNo1=None, busType1=None, arrmsg1=None, reride_Num1=None, isLast1=None,
                 vehId2=None,plainNo2=None, busType2=None, arrmsg2=None, reride_Num2=None, isLast2=None):

        self.busRouteId = busRouteId

        self.stNm = stNm # 정류소명
        self.rtNm = rtNm  # 노선명
        self.firstTm = firstTm # 첫차시간
        self.lastTm = lastTm # 막차시간
        self.term = term # 배차간격 (분)

        self.paramId1 = paramId1 # 첫번째 도착 예정 차량 파라미터
        self.vehId1 = vehId1  # 도착예정버스ID
        self.plainNo1 = plainNo1  # 도착예정버스의 차량유형
        self.busType1 = busType1  # 첫번째 도착예정 버스의 도착정보메시지
        self.arrmsg1 = arrmsg1  # 첫번째 도착예정 버스의 도착정보메시지
        self.reride_Num1 = reride_Num1  # 첫번째 도착예정 버스의 버스내부 제공용 현재 재차 인원
        self.isLast1 = isLast1  # 도착예정버스의 막차여부

        self.paramId2 = paramId2  # 두번째 도착 예정 차량 파라미터
        self.vehId2 = vehId2  # 도착예정버스ID
        self.plainNo2 = plainNo2  # 도착예정버스의 차량유형
        self.busType2 = busType2  # 첫번째 도착예정 버스의 도착정보메시지
        self.arrmsg2 = arrmsg2  # 첫번째 도착예정 버스의 도착정보메시지
        self.reride_Num2 = reride_Num2  # 첫번째 도착예정 버스의 버스내부 제공용 현재 재차 인원
        self.isLast2 = isLast2  # 도착예정버스의 막차여부


    def __str__(self):
        s = ''
        s += '노선 고유번호: ' + self.busRouteId + '\n'
        s += '정류소명: ' + self.stNm + '\n'
        s += '노선명: ' + self.rtNm + '\n'
        s += '첫차시간: ' + self.firstTm + '\n'
        s += '막차시간: ' + self.lastTm + '\n'
        s += '배차간격: ' + self.term + '\n'

        s += '첫번째 도착예정버스 호출 파라미터: ' + self.paramId1 + '\n'
        s += '첫번째 도착예정버스ID: ' + self.vehId1 + '\n'
        s += '첫번째 도착예정버스의 차량번호: ' + self.plainNo1 + '\n'
        s += '첫번째 도착예정버스의 차량유형: ' + self.busType1 + '\n'
        s += '첫번째 도착예정 버스의 도착정보메시지: ' + self.arrmsg1 + '\n'
        s += '첫번째 도착예정 버스의 버스내부 제공용 현재 재차 인원: ' + self.reride_Num1 + '\n'
        s += '첫번째 도착예정버스의 막차여부: ' + self.isLast1 + '\n'

        s += '두번째 도착예정버스 호출 파라미터: ' + self.paramId2 + '\n'
        s += '두번째 도착예정버스ID: ' + self.vehId2 + '\n'
        s += '두번째 도착예정버스의 차량번호: ' + self.plainNo2 + '\n'
        s += '두번째 도착예정버스의 차량유형: ' + self.busType1 + '\n'
        s += '두번째 도착예정 버스의 도착정보메시지: ' + self.arrmsg2 + '\n'
        s += '두번째 도착예정 버스의 버스내부 제공용 현재 재차 인원: ' + self.reride_Num2 + '\n'
        s += '두번째 도착예정버스의 막차여부: ' + self.isLast2 + '\n'
        return s

class Bus3:
    def __init__(self,  busRouteId=None, seq=None, stationNm=None, direction=None,
                 gpsX=None, gpsY=None, busRouteNm=None):

        self.busRouteId = busRouteId # 버스 고유번호

        self.seq = seq # 순번
        self.stationNm = stationNm # 정류소명
        self.direction = direction # 진행방향
        self.gpsX = gpsX # x좌표
        self.gpsY = gpsY # y좌표
        self.busRouteNm = busRouteNm # 노선명



    def __str__(self):
        s = ''
        s += '버스 고유번호: ' + self.busRouteId + '\n'
        s += '순번: ' + self.seq + '\n'
        s += '정류소명: ' + self.stationNm + '\n'
        s += '진행방향: ' + self.direction + '\n'
        s += 'x좌표: ' + self.gpsX + '\n'
        s += 'y좌표: ' + self.gpsY + '\n'
        s += '노선명: ' + self.busRouteNm + '\n'

        return s