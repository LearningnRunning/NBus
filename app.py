from flask import Flask, render_template,request

from bus_info.service import Service
from routes.bus_route import bp as bus_bp
from routes.mem_route import bp as mem_bp
from routes.res_route import bp as res_bp
import requests, json

def current_location():
    here_req = requests.get("http://www.geoplugin.net/json.gp")

    if (here_req.status_code != 200):
        print("현재좌표를 불러올 수 없음")
    else:
        location = json.loads(here_req.text)
        crd = {"lat": str(location["geoplugin_latitude"]), "lng": str(location["geoplugin_longitude"])}

    return crd

service = Service()

app = Flask(__name__)

app.secret_key = 'ram'

# url이 등록된 bluePrint 객체 등록
# 블루 프린트에 등록한 url을 flask객체가 인식
# 모든 URL을 한 app.py에 등록하면 관리가 어려워 블루프린트를 사용한다.
# 단위 별로 끊어서 url 관리
app.register_blueprint(bus_bp)
app.register_blueprint(mem_bp)
app.register_blueprint(res_bp)

@app.route('/')
def root():
    '''
    로그인 처리
    session['flag'] = True
    session['loginid'] = id
    로그아웃 처리
    session.pop('flag')
    session.pop('loginid')'''
    tmX = 126.8973568
    tmY = 37.51936
    radius = 300
    res = service.getStationByPos(tmX, tmY, radius)
    return render_template('index.html', res=res, flag=True)

if __name__ == '__main__':
    app.run(debug=True) #
