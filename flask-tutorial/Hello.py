from flask import Flask # 플라스크 객체 불러오기
app = Flask(__name__)

# route decorator (귀찮으니 annotation 이라고 부르자)
# 함수를 URL과 연결시켜 주는 기능을 함
# app.route(rule,method)
@app.route('/') 
def hello_world():
   return 'Hello World!'


# decorator 대신 app객체의 add_url_rule 메소드도 있다
# app.add_url_rule(URL,endpoint,func)
# endpoint : flask가 함수의 이름을 저장하는 공간
def hello_codybuilder() :
    return 'Hello Codybuilder'
app.add_url_rule('/codybuilder','h',hello_codybuilder)

# 동적 라우팅 (with string)
@app.route('/hello/<name>') # URL에 <>로 변수 설정
def hello_name(name) : # 해당 변수를 함수의 argument로 받음
    value_type = type(name)
    return f"당신이 URL창에 쓴 것은 {name} 이고 타입은 {value_type}입니다."

# 동적 라우팅 with other type
@app.route('/blog/<int:postID>')
def show_blog(postID):
    value_type = type(postID)
    return 'Blog Number %d %s' % (postID,value_type)

@app.route('/rev/<float:revNo>')
def revision(revNo):
    value_type = type(revNo)
    return 'Revision Number %f %s' % (revNo,value_type) # Front화면에서는 11.500000과 같이 표현됨

# URL rule 작성시 주의점 : 끝에 / 붙이는것과 안 붙이는 것이 다르다.
@app.route('/flask') # 브라우저에 /flask/라고 치면 404 발생
def hello_flask():
   return 'Hello Flask'

@app.route('/python/') # 브라우저에 /python까지만 쳐도 리다이렉트 됨
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
#    app.run() # Flask 객체를 실행시킴. app.run(host,port,debug,options)
   app.run(debug=True) #수정사항이 있을 경우, 자동으로 재기동해주는 옵션