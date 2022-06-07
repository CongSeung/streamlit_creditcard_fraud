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

![image](https://user-images.githubusercontent.com/105832386/172273027-3e2b553b-0522-4c0f-b3fd-b46cf1570821.png)

## Data EDA / 데이터 탐색하기
신용카드 사기의 특징에 대해 알아보자.

## Determination of Fraud / 사기 여부 판단하기

사용 방법

사기여부를 판단하기 위해 필요한 데이터는 다음과 같다.

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

거리를 구하기 위해서
geopy 라이브러리를 사용하였고,
먼저 주소 데이터를 위도 경도로 반환하는 함수를 만든 후에
두 장소의 주소를 사용자로부터 입력받아 거리를 구할 수 있도록 구성하였다.






  












***
    
     
     with st.expander("장소 간 거리를 모를 때는 이 곳을 눌러주십시요."):
          address1 = st.text_input('첫번째 주소 입력:(예시 : oo시 oo구 oo로oo번길 oo)')
                 address2 = st.text_input('두번째 주소 입력:(예시 : oo시 oo구 oo로oo번길 oo)')
                 b1 = st.button('입력하기',key="1")
                 if b1 :
                     lat_01 = geocoding(address1)[0]
                     lng_01 = geocoding(address1)[1]
                     st.text('첫번째 장소의 위도 : {}, 경도 : {}'.format(lat_01,lng_01))

                     lat_02 = geocoding(address2)[0]
                     lng_02 = geocoding(address2)[1]
                     st.text('두번째 장소의 위도 : {}, 경도 : {}'.format(lat_02,lng_02))

                     map_data = pd.DataFrame({'latitude':[lat_01, lat_02],'longitude':[lng_01, lng_02]})
                     st.map(data= map_data, zoom = 9)

                     coords_1 = (lat_01, lng_01)
                     coords_2 = (lat_02, lng_02)

                     st.subheader('두 지점 사이의 거리는 ')
                     st.subheader('{} 입니다.'.format(geopy.distance.geodesic(coords_1, coords_2)))

***
두 좌표의 거리를 구하기 위해 geopy의 distance 라이브러리를 이용하였다.

---------------------------

표준 구매 가격 대비 매입 가격 비율은 다음과 같이 구성하였다.

***
     price_1 = st.number_input('매입 가격',1, 999999999)
     price_2 = st.number_input('표준 가격',1, 999999999)
     price_3 = price_1/price_2
***
