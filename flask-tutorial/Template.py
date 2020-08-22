from flask import Flask
from flask import redirect, url_for # 리다이렉트 함수 불러오기
from flask import request # 리퀘스트 객체를 불러오기
from flask import render_template # 템플릿 호출을 위한 함수 불러오기

# 템플릿 폴더는 Flask 객체 생성시에 설정된다
# 따로 선언하지 않으면 app = Flask(__name__, template_folder = 'templates')로 자동 설정된다
# 해당 templates폴더는, 스크립트와 동일한 폴더 내에 있어야 한다.
#app = Flask(__name__)  

# 원하는 경로가 있다면, 마찬가지로 스크립트위치 기준 상대경로로 지정해준다
app = Flask(__name__,template_folder = 'template') 

@app.route('/html')
def html() :
    # 가장 원시적인 방식이지만, 플라스크는 html 구문 그 자체를 return할 수도 있다!
    # 물론 실제로는 이렇게 하지 않는다
    # 이유 : python - html, 더 나아가 백엔드 - 프론트엔드 간의 역할 분리를 위함
    return '<html><body><h1>Hello World (with h1 tag)</h1></body></html>'

@app.route('/jinja2/<user>')
def jinja2(user) :
    # render_template 함수로 이미 존재하는 html파일 리턴 가능
    # 그럼 브라우저에서 알아서 렌더링 해 주겠지?
    return render_template('hello.html',name=user)# 해당 이름의 파일을 template_folder 폴더 내에서 찾는다
    
    #return render_template('../hello.html') # 여기에서 ../ 를 써도 소용이 없다. 해당 내용을 파일 이름으로 해석하기 때문
    #return render_template('/python-practice/flask-tutorial/templates/hello.html') #절대경로도 소용없다

@app.route('/jinja2/<int:score>')
def hello_score(score) :
    return render_template('hello_score.html',marks=score)


if __name__ == '__main__':
#    app.run() # Flask 객체를 실행시킴. app.run(host,port,debug,options)
   app.run(debug=True) #수정사항이 있을 경우, 자동으로 재기동해주는 옵션