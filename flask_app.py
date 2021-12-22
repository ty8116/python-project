from flask import Flask, render_template
from urllib import request
from bs4 import BeautifulSoup
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template('index.html', subject="안녕하세요. 반갑습니다. 최태영 입니다")
 
#1-1
@app.route('/<user>')
def hello(user):
    return '<h1> hello ' + user
 
#2 html 연결 - 본인 소개 또는 시각화 결과 페이지
@app.route("/about")
def about():
    return render_template('img_test.html', image_file='img/다운로드.PNG')
 
#3 이미지1 - 자기가 좋아하는 사람 등등 사진
@app.route("/show1")
def show1():
    return render_template('img_test1.html', image_file='img/캡처.PNG')
 
#3 이미지2 - 크리스마스 카드 for 쌤
@app.route("/show2")
def show2():
    return render_template('img_test2.html', image_file='img/christmas.jpg')
 
 
#4 기상청1(전국중기예보)
@app.route("/kma")
def kma():
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=108")
    # BeautifulSoup를 사용해 웹 페이지를 분석합니다.
    soup = BeautifulSoup(target, "html.parser")
 
    # location 태그를 찾습니다.
    output = ""
    for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}</br>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}".format(location.select_one("tmn").string, location.select_one("tmx").string)
        output += "<hr/>"
 
    return output



#5 기상청2(경상남북도 중기예보)
@app.route("/kma1")
def kma1():
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=108")
 
    # BeautifulSoup를 사용해 웹 페이지를 분석합니다.
    soup = BeautifulSoup(target, "html.parser")
 
    # location 태그를 찾습니다.
    output = ""
 
    # 제목발표날짜 출력
    for item in soup.select("item"):
        output += "<h2>{}</h2><hr/>".format(item.select_one("title").string)
   
    for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx, tmEf 태그를 찾아 출력합니다.
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날짜: {}</br>".format(location.select_one("tmEf").string)
        output += "날씨: {}</br>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}".format(location.select_one("tmn").string, location.select_one("tmx").string)
        output += "<hr/>"
 
  # 제목, 날짜, 지역, 세부정보 출력
    output += "{}</br>".format(soup.select_one("title").string)
    output += "날짜: {}</br>".format(location.select_one("tmEf").string)  
    output += "지역: {}</br>".format(soup.select_one("province").string)
 
    return output


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
