from flask import Blueprint, render_template, request

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
    arsId = id.split('@')[0]
    stId = id.split('@')[1]
    tmp_res = service.getRouteByStation(arsId)
    res = []
    for i in tmp_res:
        tmp_lst3 = service.getStaionByRoute(i, stId)
        res.extend(service.getArrInfoByRoute(tmp_lst3[0], tmp_lst3[1], tmp_lst3[2]))
    return render_template('bus/stationList.html', res=res)

@bp.route('/buslistByStation', methods=['POST'])
def buslistByStation():
    arsId = request.form['arsId']
    res = service.getBusInfoByStationId(arsId)
    return render_template('bus/busList.html', res=res, flag=True)

@bp.route('/buslistByStation/<string:arsId>', methods=['GET'])
def buslistByStation2(arsId):
    res = service.getBusInfoByStationId(arsId)
    return render_template('bus/busList.html', res=res, flag=True)

