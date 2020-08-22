from flask import Flask
from flask import redirect, url_for # 리다이렉트 함수 불러오기
from flask import request # 리퀘스트 객체를 불러오기
from flask import render_template # 템플릿 호출을 위한 함수 불러오기
from flask import make_response

app = Flask(__name__)

@app.route('/cookie')
def index():
   return render_template('cookie.html')

@app.route('/setcookie',methods = ['GET','POST'])
def setcookie() :
    if request.method == 'POST':
        user = request.form['nm']

        cookie_nm = 'userID'
        resp = make_response(render_template('setcookie.html',cookie_nm = cookie_nm))
        resp.set_cookie(cookie_nm,user)
        
        return resp

@app.route('/getcookie')
def getcookie() :
    name = request.cookies.get('userID')
    return render_template('getcookie.html', name = name )

if __name__ == '__main__' :
    app.run(debug=True)