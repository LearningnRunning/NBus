from flask import Blueprint, render_template, request, session

from bus_info.service import Service

service = Service()

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


@bp.route('/arrstationinfo/<string:id>', methods=['GET'])
def arrinfo(id):
    res = service.getAllStaionByRoute(id)
    return render_template('bus/res_arr.html', res=res)

