from flask import Blueprint, render_template, request, session

from reservation.service import ReService
from reservation.vo import Reserve

from bus_info.service import Service
from bus_info.vo import Bus1, Bus2

rservice = ReService()
bservice = Service()

# 블루 프린트 생성, 블루 프린트는 라우트 등록 객체.
bp = Blueprint('reserve', __name__, url_prefix='/reserve')

@bp.route('/reserveinfo', methods=['GET'])
def checkForm():
    loginid = session['loginid']
    check = rservice.getById(id=loginid)
    return render_template('bus/reservation.html', check=check, flag=True)


