from flask import Flask
from flask import redirect, url_for # 리다이렉트 함수 불러오기
from flask import request # 리퀘스트 객체를 불러오기
from flask import render_template # 템플릿 호출을 위한 함수 불러오기
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy 객체 불러오기

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '' # app.config에 저장해두고 쓰는 듯

db = SQLAlchemy(app) # SQLAlchemy 객체 생성, argument로 app을 넣어준다.
class students(db.Model) : # Model 을 이용한 객체 생성 완료
    id = db.Column('student_id',db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self,name,city,addr,pin) :
        self.name = name
        self.city = name
        self.addr = name
        self.pin = name

@app.route('/')
def show_all() :
    return render_template('show_all.html',students = students.query.all())

@app.route('/new', methods = ['GET','POST'])
def new() :
    if request.method == 'GET' :
        if not request.form['name'] or not request.form['city'] or
            not request.form['addr'] :
            flash('Please enter all the fields','error') # 이 부분 해석 필요
        else :
            student = students(request.form['name'],request.form['city'],
                request.form['addr'],request.form['pin'])
            
            db.session.add(student)
            db.session.commit()
            flash()