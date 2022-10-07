from flask import Blueprint, render_template, request, session
from member.service import MemberService
from bus_info.service import Service
from reserve.service import ResService
from datetime import datetime

from reserve.vo import Reserve
service = Service()
memservice = MemberService()
reservice = ResService()


# 블루 프린트 생성, 블루 프린트는 라우트 등록 객체.
bp = Blueprint('bus', __name__, url_prefix='/bus')

@bp.route('/businfo', methods=['POST'])
def businfo():
    strSrch = request.form['strSrch']
    res = service.getStationByName(strSrch)
    return render_template('bus/busList.html', res=res, flag=True)

@bp.route('/stationinfo/<string:id>', methods=['GET'])
def stationinfo(id):
    arsId = id.split('@')[0] # 정류소 고유번호
    stId = id.split('@')[1]  # 정류소아이디

    tmp_res = service.getRouteByStation(arsId)

    res = []
    for i in tmp_res:
        tmp_lst3 = service.getStaionByRoute(i, stId)
        # [stId:정류소아이디, busRouteId:노선ID, seq:순번] 추가
        res.extend(service.getArrInfoByRoute(tmp_lst3[0], tmp_lst3[1], tmp_lst3[2]))

    return render_template('bus/stationList.html', res=res)


@bp.route('/arrstationinfo/<string:paramId>', methods=['GET'])
def arrinfo(paramId):
    # paramId1 = stId + '@' + busRouteId + '@' + seq + '@' + plainNo1 + '@' + reride_Num1 + '@' + busType1
    # paramId2 = stId + '@' + busRouteId + '@' + seq + '@' + plainNo2 + '@' + reride_Num2 + '@' + busType2

    ##### 이어붙인 변수들 split
    stId = paramId.split('@')[0]
    busRouteId = paramId.split('@')[1]
    seq = paramId.split('@')[2]
    plainNo = paramId.split('@')[3]
    reride_Num = paramId.split('@')[4]
    busType = paramId.split('@')[5]

    ##### 필요한 api 호출
    res = service.getAllStaionByRoute(busRouteId)
    res2 = service.getArrInfoByRoute(stId, busRouteId, seq)
    loginid = session['loginid']
    m = memservice.getById(id=loginid)

    ##### db에 insert 할 값 정의
    resdate = datetime.now()
    id = m.id
    rtNm = res2[0].rtNm
    stNm = res2[0].stNm
    # stNmD =
    plainNo = plainNo
    etc = '-'

    # reserve 가능 조건
    if (busType == '저상') and (reride_Num == '여유' or '보통'):
        session['flag'] = True
        reserve = 'True'
        print("예약이 완료되었습니다.")
        reservice.addReserve(Reserve(resdate=resdate, id=id, plainNo=plainNo, rtNm=rtNm,
                                     stNm=stNm, reserve=reserve, etc=etc))

    else:
        print("예약 할 수 없는 차량입니다.")

    return render_template('bus/res_arr.html', res=res)


# @bp.route('/reservationinfo/<string:stationNm>', methods=['GET'])
# def reservationinfo(stationNm):
#
#
#     return render_template('bus/reservationinfo.html')

