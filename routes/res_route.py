from flask import Blueprint, render_template, request, session, redirect
from reserve.service import ResService

service = ResService()

# 블루 프린트 생성, 블루 프린트는 라우트 등록 객체.
bp = Blueprint('reserve', __name__, url_prefix='/reserve')

@bp.route('/reserveinfo', methods=['GET'])
def reserveForm():
    loginid = session['loginid']
    todayres = service.getByDate(id=loginid)
    res = service.getByDatePast(id=loginid)
    return render_template('reserve/reservation.html', todayres=todayres, res=res)

@bp.route('/reserveinfo', methods=['POST'])
def out():
    reservenum = request.form.get('reservenum')
    service.delReserve(reservenum=reservenum)
    return redirect('/')