from flask import Flask
from flask import redirect, url_for # 리다이렉트 함수 불러오기

app = Flask(__name__)
@app.route('/')
def hello() :
    return 'nothing'

@app.route('/admin') # 에러 : 분명 /admin이라고 쳤는데 자동 /admin/ 으로 리다이렉트됨. 왜?
def hello_admin() :
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest) :
    return f'Hello {guest} as Guest'

@app.route('/user/<name>')
def hello_user(name) :
    if name == 'admin' :
        # url_for에 들어가는 인자는, 함수 이름을 문자열로 감싼 것
        return redirect(url_for('hello_admin')) 
        # 함수 이름을 그대로 넣으면 에러가 뜬다. 
        # 이유 : flask의 endpoint에서 해당 문자열을 찾는 식으로 수행되는데, 함수 객체 그대로 넣으면 못 찾음
        #return redirect(url_for(hello_admin)) 
    else :
        return redirect(url_for('hello_guest',guest=name)) #  url_for 내에서 매개변수 연결도 가능하다

if __name__ == '__main__':
#    app.run() # Flask 객체를 실행시킴. app.run(host,port,debug,options)
   app.run(debug=True) #수정사항이 있을 경우, 자동으로 재기동해주는 옵션