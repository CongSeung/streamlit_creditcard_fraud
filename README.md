# streamlit_creditcard_fraud / 신용카드 결제 사기 확인하기

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

거래 장소와의 거리 등 사전에 준비되지 않은 정보를 위해 
거래 장소의 주소를 입력하여 두 장소의 거리를 구하는 기능과
거래 금액과 표준 금액의 비율을 구하는 기능을 함께 구현하여 놓았다.

거리를 구하기 위해 주소를 
***

     def geocoding(address):
            geo = geo_local.geocode(address)
            x_y = [geo.latitude, geo.longitude]
            return x_y
            
***



  





