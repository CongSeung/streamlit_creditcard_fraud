# streamlit_creditcard_fraud / 신용카드 결제 사기 확인하기

신용카드 사기 여부를 판단하기 위해 
Streamlit을 이용해 구성한 웹 대시보드입니다.


## columns / 컬럼 정보

distance_from_home - 홈으로부터 거래가 발생한 곳과의 거리입니다. (단위 : km)

distance_from_last_transaction - 마지막 거래로부터의 거리입니다. (단위 : km)

ratio_to_median_purchase_price - 중앙 구매 가격 대비 매입 가격 거래 비율입니다.

repeat_retailer - 거래가 동일한 소매점에서 발생하였습니까?

used_chip - 칩(신용카드)을 통한 거래입니다.
     
used pinnumber - PIN 번호를 사용하여 거래가 발생했는지 여부를 나타냅니다.

online_order - 거래가 온라인 주문입니다.

fraud - 거래가 정상이면 0 / 사기건이면 1 입니다.

------------------------------------------------------

## Data EDA / 데이터 탐색하기
신용카드 사기의 특징에 대해 알아보자.

![image](https://user-images.githubusercontent.com/105832386/172541014-e027b46d-b0e2-4925-bb64-c4f15b002488.png)
라디오 버튼을 이용해 보고싶은 데이터프레임을 고를 수 있다.

![image](https://user-images.githubusercontent.com/105832386/172541173-87dfddfa-797e-41e9-8776-35a1842d1934.png)
컬럼의 종류가 많아 확인하기 힘들 땐 원하는 컬럼만 비교하여 볼 수 있다.

![image](https://user-images.githubusercontent.com/105832386/172541262-a602e2f8-95fa-4d8b-bd8f-f3ca61fd98a9.png)
체크 박스를 이용해 비주얼라이징 된 데이터를 확인할 수 있다. 

-------------------------------------------------------

- 거래장소와 집까지의 거리, 단위: km
- 거래장소와 마지막 거래로부터의 거리, 단위: km
- 가격 대비 매입 가격 비율
- 거래가 동일한 소매점에서 발생하였는지
- 칩(신용카드)을 통한 거래인지
- PIN 번호를 통한 거래인지
- 온라인으로 거래되었는지 

위 데이터를 좌측 사이드바 메뉴에 형식에 맞게 입력해준다.



페이지 메인에는    
사용자가 입력할 데이터 중       
거래 장소와의 거리 등 확인하기 어려운 정보에 도움을 주기 위해    
거래 장소의 주소를 입력하여 두 장소의 거리를 구하는 기능과     
거래 금액과 표준 금액의 비율을 구하는 기능을 함께 구현하여 놓았다.    

***
     from geopy.geocoders import Nominatim
     import geopy.distance

     def geocoding(address):
            geo = geo_local.geocode(address)
            x_y = [geo.latitude, geo.longitude]
            return x_y
     
     
     geopy.distance.geodesic()
***

![image](https://user-images.githubusercontent.com/105832386/172540786-9628be34-de6a-46d3-83bb-9ca405c7498b.png)


거리를 구하기 위해서   
geopy 라이브러리를 사용하였고,   
먼저 주소 데이터를 위도 경도로 반환하는 함수를 만든 후에   
두 장소의 주소를 사용자로부터 입력받아 거리를 구할 수 있도록 구성하였다.   


![image](https://user-images.githubusercontent.com/105832386/172540713-66a62ad7-895f-4907-a53d-39b967606cae.png)

데이터를 알맞게 입력한 후에 확인하기 버튼을 누르면 페이지 메인에 정상적인 결제인지, 사기성 결제인지 문구가 출력된다.
