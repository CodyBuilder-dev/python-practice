from flask import Flask
from flask import redirect, url_for # 리다이렉트 함수 불러오기
from flask import request # 리퀘스트 객체를 불러오기
from flask import render_template # 템플릿 호출을 위한 함수 불러오기
from werkzeug.utils import secure_filename # 단순 파일네임 말고 이쪽 쓰는 것을 추천하던데, 이유는 모르겠음

app = Flask(__name__)

# 아무런 설정이 없는 경우, 파일은 Flask app 위치에 저장됨
# app.config['UPLOAD_FOLDER']에 경로를 저장해두고 나중에 호출해서 쓰는 식으로 해결
# app.config['UPLOAD_FOLDER']의 설정을 flask가 인식하지는 않음
app.config['UPLOAD_FOLDER'] = 'uploads/' # 앞에는 / 없이, 뒤에는 / 붙여서 적어줘야 함

# 파일 관련 옵션 추후 조사 예정

@app.route('/')
def redirect_main() :
    return redirect(url_for("upload"))

@app.route('/upload')
def upload():
   return render_template('upload.html')

@app.route('/upload-file', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
        print("리퀘스트의 files 속성" ,  request.files)
        print("리퀘스트의 files 타입" ,  type(request.files))
        f = request.files['file'] # 리퀘스트의 files 속성을 꺼냄
        
        print("files속성 내의 file 속성명 " , f)
        print("files속성 내의 file 속성타입 " , type(f))
      
        # f.save() # 저장할 파일의 경로+이름을 argumnet로 넣어 준다.
        f.save(app.config['UPLOAD_FOLDER']+f.filename) # 원본 파일의 이름/형식 그대로 저장
        # f.save(app.config['UPLOAD_FOLDER']+secure_filename(f.filename)) # encrypted된 파일 형태로 저장
        return 'file uploaded successfully'

if __name__ == '__main__':
    print(app.config)
    app.run(debug=True) #수정사항이 있을 경우, 자동으로 재기동해주는 옵션
    