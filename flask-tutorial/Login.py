from flask import Flask
from flask import redirect, url_for # 리다이렉트 함수 불러오기
from flask import request # 리퀘스트 객체를 불러오기

app = Flask(__name__)

@app.route('/success/<name>')
def success(name) :
    return 'welcome to %s' % name


@app.route('/login',methods = ['GET','POST'])
def login() :
    if request.method == 'POST' :
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else :
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))

if __name__ == '__main__':
#    app.run() # Flask 객체를 실행시킴. app.run(host,port,debug,options)
   app.run(debug=True) #수정사항이 있을 경우, 자동으로 재기동해주는 옵션