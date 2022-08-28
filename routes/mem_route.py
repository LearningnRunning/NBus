from flask import Blueprint, render_template, request, session, redirect

from member.service import MemberService
from member.vo import Member

service = MemberService()

# 블루 프린트 생성, 블루 프린트는 라우트(요청 url) 등록 객체.
bp = Blueprint('mem', __name__, url_prefix='/member')
# bp = Blueprint('이름', __name__, url_prefix='/자동으로 붙을 주소')

@bp.route('/join', methods=['GET'])
def joinForm():
    return render_template('member/join.html')

@bp.route('/join', methods=['POST'])
def join():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']
    service.addMember(Member(id=id,pwd=pwd,name=name,email=email))
    return render_template('index.html')

# 로그인
@bp.route('/login', methods=['GET'])
def loginForm():
    return render_template('member/login.html')

@bp.route('/login', methods=['POST'])
def login():
    id = request.form['id']
    pwd = request.form['pwd']
    m = service.getById(id=id)
    if m != None and m.pwd == pwd:
        session['flag']=True
        session['loginid']=id
    return render_template('index.html')

#로그아웃
@bp.route('/logout', methods=['GET'])
def logout():
    session.pop('flag')
    session.pop('loginid')
    return render_template('index.html')

# 내정보수정
@bp.route('/myinfo', methods=['GET'])
def editForm():
    loginid = session['loginid']
    m = service.getById(id=loginid)
    return render_template('member/edit.html', m=m)

@bp.route('/myinfo', methods=['POST'])
def edit():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']
    service.addMember(Member(id=id, pwd=pwd, name=name, email=email))
    return render_template('index.html')

# 탈퇴
@bp.route('/out', methods=['GET'])
def out():
    loginid = session['loginid']
    service.delMember(id=loginid)
    return redirect('/member/logout')

