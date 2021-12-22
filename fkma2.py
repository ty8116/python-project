# 모듈을 읽어 들입니다.
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup
 
# 웹 서버를 생성합니다.
app = Flask(__name__)
@app.route("/")
 
def hello():
  # urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
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
