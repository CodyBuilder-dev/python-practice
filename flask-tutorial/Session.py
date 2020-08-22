from flask import Flask
from flask import redirect, url_for # 리다이렉트 함수 불러오기
from flask import request # 리퀘스트 객체를 불러오기
from flask import render_template # 템플릿 호출을 위한 함수 불러오기
from flask import session # session 객체 불러오기

app = Flask(__name__)
# Session을 사용하기 위해서는 Secret Key를 생성해야 한다
#app.secret_key = 'super_secret_key' # 바로 대입해도 됨
app.config['SECRET_KEY'] = 'super_secret_key'


@app.route('/')
def index():
    print(session)
    if 'username' in session:
        # session은 flask에서 dict로 저장됨   
        # key는 username, value는 
        username = session['username'] 
        
        return f"""Logged in as {username} <br> \
            <b><a href = '/logout'>click here to log out</a></b>"""
    
    return """You are not logged in <br><a href = '/login'></b>
        click here to log in</b></a>"""

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Secret Key 없이 세션에 값을 할당하려 하면 에러가 생기는 듯?
        # 
        session['username'] = request.form['username'] 
        return redirect(url_for('index'))
    return render_template('sessionLogin.html')   

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__' :
    app.run(debug = True)