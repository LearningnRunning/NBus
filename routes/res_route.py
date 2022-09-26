from flask import Blueprint, render_template, request, session, redirect

from reserve.service import ResService
from reserve.vo import Reserve

service = ResService()

# 블루 프린트 생성, 블루 프린트는 라우트 등록 객체.
bp = Blueprint('reserve', __name__, url_prefix='/reserve')

@bp.route('/reserveinfo', methods=['GET'])
def reserveForm():
    loginid = session['loginid']
    m = service.getById(id=loginid)
    return render_template('reserve/reservation.html', m=m)

@bp.route('/reserveinfo', methods=['POST'])
def checkreserve():
    reservenum = request.form['reservenum']
    id = request.form['id']
    arrmsg = request.form['arrmsg']
    rtNm = request.form['rtNm']
    plainNo = request.form['plainNo']
    stNm = request.form['stNm']
    stNmD = request.form['stNmD']
    reserve = request.form['reserve']
    etc = request.form['etc']
    service.addReserve(Reserve(reservenum=reservenum,id=id, arrmsg=arrmsg, rtNm=rtNm, plainNo=plainNo,
                                 stNm=stNm, stNmD=stNmD, reserve=reserve, etc=etc))
    return render_template('index.html')