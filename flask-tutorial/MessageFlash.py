from flask import Flask
from flask import redirect, url_for # 리다이렉트 함수 불러오기
from flask import request # 리퀘스트 객체를 불러오기
from flask import render_template # 템플릿 호출을 위한 함수 불러오기
from flask import flash # flash 불러오기

app = Flask(__name__)
# flash를 사용하려면 session이 필요하고, 이를 위해선 secret key가 있어야 한다
# session 을 import할 필요는 없다.
app.config['SECRET_KEY'] = 'superkey'

@app.route('/')
def flash_index():
   return render_template('flashIndex.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
      else:
         # flash 여러개를 쓸 경우 한번에 list화 되어 return되는 듯
         flash('You were successfully logged in.')
         flash('Hello, '+request.form['username'])
         return redirect(url_for('flash_index'))
   return render_template('flashLogin.html', error = error)

if __name__ == '__main__' :
    app.run(debug = True)