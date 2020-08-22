from flask import Flask # 플라스크 객체 불러오기
app = Flask(__name__)

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

if __name__ == '__main__':
#    app.run() # Flask 객체를 실행시킴. app.run(host,port,debug,options)
   app.run(debug=True) #수정사항이 있을 경우, 자동으로 재기동해주는 옵션