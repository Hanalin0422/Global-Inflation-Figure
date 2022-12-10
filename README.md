# Look Globe Inflation </br> - 소비자 물가 상승률 시각적 자료 자동화 프로그램 🌍

## <strong> 🖊 프로젝트 소개 </strong>

>세계 여러 나라의 CPI 상승률 정보를 이용해 상승률에 대한 차이를 한눈에 비교하기 쉽도록 <br>지구본과 Pie Chart를 통해 시각적인 자료를 자동적으로 만들어주는 프로그램이다.

<br><br>
### ⭐️ 미리 보는 프로젝트 완성 화면
<img width="722" alt="image" src="https://user-images.githubusercontent.com/78638427/206856401-f80023fd-756a-490c-83bb-fada43b875af.png">
지구본 위에 각 나라의 CPI 상승률에 따라 라벨이 원 모양으로 일정한 기준에 따라 색깔과 크기로 그 나라 위치에 표시된 모습
<br><br>

<img width="1335" alt="image" src="https://user-images.githubusercontent.com/78638427/206856860-37578501-e83e-4709-bf15-0a856ed80270.png">
Pie Chart에 각 나라 별 CPI가 표시 되어 있으며 마우스를 올릴 시 어떤 나라인지 확인할 수 있는 모습
<br><br><br><br>

> 사용한 언어

- JavaScript
- Python
> 사용한 프레임 워크 & 라이브러리  

- Node.js, Express - 서버 구성 및 Python 파일과 js 파일들 연동하는데 이용  
- EJS - 서버 화면 구성
- Globe.GL - 각 나라 위치를 label로 표시할 수 있는 지구본을 그리는 데 사용  
참고 링크 : https://globe.gl/  
참고 깃허브 : https://github.com/vasturiano/three-globe
- BeautifulSoup - 위도, 경도 사이트에서 나라의 위도, 경도 정보를 추출하는데 사용

<br><br><br><br>

## <strong> 🔌 프로그램 실행 방법  </strong>
1. npm init
2. pip3 install beautifulsoup (없을 시)
3. npm start


<br><br>
## <strong> 🖥 개발 과정 및 프로그램 동작 방식  </strong>

1. 여러 나라의 물가 상승률에 대한 자료가 필요했기에 이 자료는 inflation을 제공하는 API를 사용하였습니다.
<img width="968" alt="image" src="https://user-images.githubusercontent.com/78638427/206858436-1fa11960-76b6-4194-9792-a1e28054170d.png">


위와 같은 API를 통해
```
[
  {
    "country": "United States",
    "type": "CPI",
    "period": "june 2022",
    "monthly_rate_pct": 1.374,
    "yearly_rate_pct": 9.06
  }
]
```
이와 같이 정보를 먼저 받아옵니다.  
<br><br>

2. 
> crowling.py 📄

정보를 받아온 후 지구본에 표시를 하기 위해서는 그 나라의 위도와 경도가 필요하기 때문에 내가 가지고 있는 정보의 나라들과 위도/경도를 위도와 경도를 알려주는 사이트에서 beautifulsoup를 이용하여 크롤링을 한 뒤 json형식의 정보에 위도와 경도에 대한 자료를 추가해주었습니다.

<img width="596" alt="image" src="https://user-images.githubusercontent.com/78638427/206858772-eb7bb28b-4fd4-49e6-9dcc-14279d23b4f9.png">

위의 사진과 같이 세계 여러나라의 위도와 경도가 나와있는 사이트를 크롤링을 하여 CPI 상승률에 대한 정보를 가지고 있는 나라들을 비교하여 나에게 있는 나라들의 위도/경도 정보를 추가합니다.
<br>

![image](https://user-images.githubusercontent.com/78638427/206858853-2c32ef68-4df9-4c31-808b-b3cdbf8371e2.png)

<br><br>

3.
> main.py 📄

위도/경도를 추가한 물가 상승률이 담긴 리스트들을 받아와 각 상승률에 맞게 색깔로 표시하기 위해 기준을 두어 색을 추가하였습니다.   


|cpi | color 
|-----|--------|
cpi < 5 | blue
5<= cpi < 10 | green
10<= cpi < 15 | yellow
15<= cpi < 20 | darkorange
cpi >= 20 | red

---

![image](https://user-images.githubusercontent.com/78638427/206859049-d38abfc2-5a88-47c2-a704-9c96670199b0.png)


<strong>❌ 이때 crowling 하여 만들어낸 list는 개인 API 키를 이용하여 가져오는 자료입니다.  
그렇기 때문에 키에 대한 정보는 다른 파일로 꺼내어 git에 push 해놓지 않았기 때문에 crowling.py의 주석을 풀면 실행이 되지 않습니다.  
또한 그렇기에 main.py의 list에는 미리 얻어온 여러 나라 CPI의 정보들을 넣어놓았습니다. </strong>  
<br>

그렇게 만들어진 list는 다음과 같습니다.

```
[{'country': 'Austria', 'lat': '47.516231', 'lng': '14.550072', 'cpi': 11.047, 'color': 'yellow'}, {'country': 'Belgium', 'lat': '50.503887', 'lng': '4.469936', 'cpi': 10.629, 'color': 'yellow'}, {'country': 'Brazil', 'lat': '-14.235004', 'lng': '-51.92528', 'cpi': 6.47, 'color': 'green'}, {'country': 'Canada', 'lat': '56.130366', 'lng': '-106.346771', 'cpi': 6.88, 'color': 'green'}, {'country': 'Switzerland', 'lat': '46.818188', 'lng': '8.227512', 'cpi': 2.96, 'color': 'blue'}, {'country': 'Chile', 'lat': '-35.675147', 'lng': '-71.542969', 'cpi': 13.338, 'color': 'yellow'}, {'country': 'China', 'lat': '35.86166', 'lng': '104.195397', 'cpi': 2.172, 'color': 'blue'}, {'country': 'Czech Republic', 'lat': '49.817492', 'lng': '15.472962', 'cpi': 15.093, 'color': 'darkorange'}, {'country': 'Germany', 'lat': '51.165691', 'lng': '10.451526', 'cpi': 10.388, 'color': 'yellow'}, {'country': 'Denmark', 'lat': '56.26392', 'lng': '9.501785', 'cpi': 10.112, 'color': 'yellow'}, {'country': 'Estonia', 'lat': '58.595272', 'lng': '25.013607', 'cpi': 21.314, 'color': 'red'}, {'country': 'Spain', 'lat': '40.463667', 'lng': '-3.74922', 'cpi': 7.265, 'color': 'green'}, {'country': 'Finland', 'lat': '61.92411', 'lng': '25.748151', 'cpi': 8.311, 'color': 'green'}, {'country': 'France', 'lat': '46.227638', 'lng': '2.213749', 'cpi': 6.2, 'color': 'green'}, {'country': 'Greece', 'lat': '39.074208', 'lng': '21.824312', 'cpi': 9.065, 'color': 'green'}, {'country': 'Hungary', 'lat': '47.162494', 'lng': '19.503304', 'cpi': 22.492, 'color': 'red'}, {'country': 'Indonesia', 'lat': '-0.789275', 'lng': '113.921327', 'cpi': 5.418, 'color': 'green'}, {'country': 'Ireland', 'lat': '53.41291', 'lng': '-8.24389', 'cpi': 9.16, 'color': 'green'}, {'country': 'Israel', 'lat': '31.046051', 'lng': '34.851612', 'cpi': 5.078, 'color': 'green'}, {'country': 'India', 'lat': '20.593684', 'lng': '78.96288', 'cpi': 6.085, 'color': 'green'}, {'country': 'Iceland', 'lat': '64.963051', 'lng': '-19.020835', 'cpi': 9.333, 'color': 'green'}, {'country': 'Italy', 'lat': '41.87194', 'lng': '12.56738', 'cpi': 11.837, 'color': 'yellow'}, {'country': 'Japan', 'lat': '36.204824', 'lng': '138.252924', 'cpi': 3.804, 'color': 'blue'}, {'country': 'South Korea', 'lat': '35.907757', 'lng': '127.766922', 'cpi': 5.035, 'color': 'green'}, {'country': 'Luxembourg', 'lat': '49.815273', 'lng': '6.129583', 'cpi': 5.936, 'color': 'green'}, {'country': 'Mexico', 'lat': '23.634501', 'lng': '-102.552784', 'cpi': 8.407, 'color': 'green'}, {'country': 'Norway', 'lat': '60.472024', 'lng': '8.468946', 'cpi': 7.509, 'color': 'green'}, {'country': 'Poland', 'lat': '51.919438', 'lng': '19.145136', 'cpi': 18.036, 'color': 'darkorange'}, {'country': 'Portugal', 'lat': '39.399872', 'lng': '-8.224454', 'cpi': 10.139, 'color': 'yellow'}, {'country': 'Russia', 'lat': '61.52401', 'lng': '105.318756', 'cpi': 16.698, 'color': 'darkorange'}, {'country': 'Sweden', 'lat': '60.128161', 'lng': '18.643501', 'cpi': 10.853, 'color': 'yellow'}, {'country': 'Slovenia', 'lat': '46.151241', 'lng': '14.995463', 'cpi': 10.027, 'color': 'yellow'}, {'country': 'Slovakia', 'lat': '48.669026', 'lng': '19.699024', 'cpi': 14.892, 'color': 'yellow'}, {'country': 'Turkey', 'lat': '38.963745', 'lng': '35.243322', 'cpi': 84.389, 'color': 'red'}, {'country': 'United States', 'lat': '37.09024', 'lng': '-95.712891', 'cpi': 7.745, 'color': 'green'}, {'country': 'South Africa', 'lat': '-30.559482', 'lng': '22.937506', 'cpi': 7.778, 'color': 'green'}]
```

<br><br>

4.
> routes/index.js, views/index.ejs 📑

파이썬에서 만들어낸 리스트를 node 서버의 router로 불러 index.ejs로 전달하여 지구본을 그려주는 index.ejs화면에 데이터를 전송합니다.

![image](https://user-images.githubusercontent.com/78638427/206859723-6433f644-c182-4432-8d95-41a7d42fe52e.png)


전송된 데이터들은 위도와 경도에 맞춰 나라 이름과 물가 상승률에 따라 다른 라벨의 크기와 다른 색들을 지구본 위에 표시해줍니다.

<img width="977" alt="image" src="https://user-images.githubusercontent.com/78638427/206859931-e0b0d39b-be52-4eac-857f-608d550188e1.png">

<br><br>

5. 
> routes/statics.js, views/statics.ejs 📑

<br>
<img width="106" alt="image" src="https://user-images.githubusercontent.com/78638427/206860053-9fdb120d-9f73-47ae-aa25-6424d2d5d2a4.png">



지구본이 띄워진 화면의 오른쪽 상단 통계차트 보러가기 버튼을 누르면 Pie Chart를 통해 더 한눈에 비교할 수 있는 화면으로 넘어갈 수 있습니다.

<br>

<img width="1341" alt="image" src="https://user-images.githubusercontent.com/78638427/206860133-adfa8d8a-5332-4af7-95ef-81853f2efb05.png">


<br>

Pie Chart는 마우스를 올리면 어느 나라 인지와 그 나라의 CPI 지수를 보여줍니다.  
또한 특정 나라에 대한 정보는 빼고 Chart를 확인하고 싶다면 Chart 위의 Label들을 눌러 Chart 속의 나라를 지울 수 있습니다.




<img width="1344" alt="image" src="https://user-images.githubusercontent.com/78638427/206860258-300ab457-07e0-4063-9ffd-06cb723dee4d.png">

<br><br>

## <strong> 🔐 License </strong>
This project is licensed under the MIT License


<br><br>
## <strong> 😆 이 프로젝트를 통해 얻은 점 및 알게된 점 </strong>
- 기존 웹 크롤링 기술로 selenium만 알고 있었는데 이번 기회에 beautifulSoup라는 새로운 웹 크롤링 기술을 알게 되었고 실제 사용해보는 경험을 할 수 있었다.
- JavaScript에서 제공하는 여러 라이브러리들이 많다는 것을 알 수 있었고 그 중 프로젝트 목적에 맞는 라이브러리를 선정하여 사용해보는 경험을 할 수 있었다.
- Node.js에서 파이썬 파일을 동작시켜 결과값을 서버 템플릿인 EJS로 송출할 수 있다는 것을 알게되었고 이를 통해 앞으로 언어에 구애받지 않는 보다 다양한 프로젝트를 만들 수 있다는 것을 알게 되었다.
- 여러 곳에서 생각보다 다양한 API들을 제공하고 있다는 것을 알 수있었고 API를 실제로 사용해보는 경험을 할 수 있었다.

<br><br>

## <strong> 📚 참고자료/Reference </strong>

제공받은 이미지 
https://unpkg.com/browse/three-globe@2.24.10/example/img/

여러 나라 위도 경도를 알려주는 사이트
https://developers.google.com/public-data/docs/canonical/countries_csv

데이터 API
https://api-ninjas.com/api/inflation

웹 크롤링 문서
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

자바스크립트로 파이썬 연동 실행 방법
https://curryyou.tistory.com/225

3D 지구본 그리기
https://github.com/vasturiano/three-globe