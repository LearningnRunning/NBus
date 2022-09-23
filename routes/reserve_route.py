from flask import Blueprint, render_template, request, session, redirect

from reservation.service import ReService
from reservation.vo import Reserve

service = ReService()

# 블루 프린트 생성, 블루 프린트는 라우트 등록 객체.
bp = Blueprint('reserve', __name__, url_prefix='/reserve')

# @bp.route('/reserveinfo/<string:id>', methods=['GET'])
# def checkForm(id):
#     res = Reserve.query.get_or_404(id)
#     return render_template('bus/reservation.html', res=res)


@bp.route('/reserveinfo', methods=['GET'])
def checkForm():
    print(1)
    loginid = session['loginid']
    print(loginid)
    check = service.getById(id=loginid)
    print(check)
    return render_template('bus/reservation.html', check=check)

@bp.route('/reserveinfo', methods=['POST'])
def checkreserve():
    id = request.form['id']
    arrmsg = request.form['arrmsg']
    rtNm = request.form['rtNm']
    plainNo = request.form['plainNo']
    stNm = request.form['stNm']
    stNmD = request.form['stNmD']
    reserve = request.form['reserve']
    etc = request.form['etc']
    service.addReserve(Reserve(id=id, arrmsg=arrmsg, rtNm=rtNm, plainNo=plainNo,
                                 stNm=stNm, stNmD=stNmD, reserve=reserve, etc=etc))
    return render_template('index.html')
