import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import streamlit as st
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  confusion_matrix, accuracy_score
from geopy.geocoders import Nominatim
import geopy.distance

def run_ml():

    s_scaler = joblib.load('data/card_fra_scaler.pkl')
    classifier = joblib.load('data/card_fra_classifier.pkl')

    home_dist = st.sidebar.number_input('거래장소와 집까지의 거리, 단위: km')
    last_dist = st.sidebar.number_input('거래장소와 마지막 거래로부터의 거리, 단위: km')
    medi_purchase = st.sidebar.number_input('표준 구매 가격 대비 매입 가격 비율')
    
    my_order = ['네', '아니오']      
    ##### Radio 1
    status_01 = st.sidebar.radio('거래가 동일한 소매점에서 발생하였습니까?', my_order)  

    if status_01 == my_order[0] :
        retailer = 1
      
    elif status_01 == my_order[1] :
        retailer = 0
    
    ##### Radio 2
    status_02 = st.sidebar.radio('칩(신용카드)을 통한 거래입니까?', my_order)  

    if status_02 == my_order[0] :
        used_chip = 1
      
    elif status_02 == my_order[1] :
        used_chip = 0
    
    ##### Radio 3
    status_03 = st.sidebar.radio('PIN 번호를 통한 거래입니까?', my_order)  

    if status_03 == my_order[0] :
        used_pinnumber = 1
      
    elif status_03 == my_order[1] :
        used_pinnumber = 0
    
    ##### Radio 4
    status_04 = st.sidebar.radio('온라인 거래입니까?', my_order)  

    if status_04 == my_order[0] :
        online_order = 1
      
    elif status_04 == my_order[1] :
        online_order = 0

    if st.sidebar.button('확인해보기'):
        new_data = ( home_dist, last_dist, medi_purchase, retailer, used_chip, used_pinnumber, online_order)

        new_data = np.array(new_data)
        new_data = new_data.reshape(1, -1)
        new_data = s_scaler.transform(new_data)
        result = classifier.predict(new_data)

        if result == 0 :
            st.title('이 카드 결제는 정상적인 결제입니다.')
        else :
            st.title('이 카드 결제는 신용카드 사기입니다.')

    st.subheader('카드 결제 건의 사기 여부를 판별할 수 있습니다.')
    st.subheader('아래 준비된 도구를 이용해 좌측 메뉴에 값을 넣고 확인해보기를 눌러주십시오.')

    with st.container():
        geo_local = Nominatim(user_agent='South Korea')

        # 위도, 경도 반환하는 함수
        def geocoding(address):
            geo = geo_local.geocode(address)
            x_y = [geo.latitude, geo.longitude]
            return x_y
        
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
    
    st.text('########################################################')


    with st.expander("표준 구매 가격 대비 매입 가격 비율을 계산하려면 이 곳을 눌러주십시요."):
        st.text('표준 구매 가격 대비 매입 가격 비율은 매입 가격 / 표준 구매 가격 대비 입니다.')
        st.text('아래에서 구한 값을 좌측 메뉴 - 표준 구매 가격 대비 매입 가격 비율에 입력하여 주십시오.')
        price_1 = st.number_input('매입 가격',1, 999999999)
        price_2 = st.number_input('표준 가격',1, 999999999)
        price_3 = price_1/price_2
        st.subheader('표준 구매 가격 대비 매입 가격 비율은 <{}> 입니다.'.format(price_3))
    

    
    
    