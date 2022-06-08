import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import streamlit as st
from PIL import Image

def run_eda():
    st.text('과거 데이터를 분석해보자.')
    
    df = pd.read_csv('data/card_transdata.csv')
    
    st.subheader('머신러닝 학습에 사용된 데이터셋')
    
    # 데이터프레임 확인용 라디오 버튼
    my_order = ['데이터셋 보기', '기본 통계자료 보기']   

    status = st.sidebar.radio('자료 선택', my_order)  # 라디오 버튼은 1과 0이 아닌 들어가 있는 값을 띄게 된다.

    if status == my_order[0] :
        st.dataframe(df)
    elif status == my_order[1] :
        st.dataframe(df.describe())

    # 선택한 컬럼만 확인하기
    mul_column = st.sidebar.multiselect('선택한 컬럼만 보기', df.columns.to_list())

    if st.sidebar.button('선택 컬럼 확인하기'):
        st.dataframe(df[mul_column])
    
    # 히스토그램 확인
    if st.sidebar.checkbox('히스토그램 확인하기'):
        img = Image.open('data/countplot.png')

        st.image(img,use_column_width=True)

    # 상관관계 확인 : pairplot
    if st.sidebar.checkbox('상관관계 확인하기'):
        img = Image.open('data/pairplot.png')

        st.image(img,use_column_width=True)
    
    fraud_col = ['repeat_retailer', 'used_pin_number', 'used_chip', 'online_order']

    choice = st.sidebar.selectbox('fraud와 주요컬럼의 데이터 확인',fraud_col)

    if st.sidebar.button('확인하기'):
        if choice == fraud_col[0]:
            img = Image.open('data/re_fr.png')
            st.image(img,use_column_width=True)
        elif choice == fraud_col[1]:
            img = Image.open('data/pin_fr.png')
            st.image(img,use_column_width=True)
        elif choice == fraud_col[2]:
            img = Image.open('data/us_fr.png')
            st.image(img,use_column_width=True)
        elif choice == fraud_col[3]:
            img = Image.open('data/or_fr.png')
            st.image(img,use_column_width=True)

    #### 원래 함수 ec2 에서 돌리기 너무 무거워 죽여놓음
    # select = st.sidebar.selectbox('히스토그램 확인하기', df.columns.to_list())

    # if st.sidebar.button('히스토그램 확인하기'):
    #     fig1 = plt.figure() 
    #     sns.countplot(data = df , x = select)
    #     st.pyplot(fig1)

    # mul_select = st.sidebar.multiselect('상관관계 분석 / 컬럼 2개 선택',df.columns.to_list())

    # if st.sidebar.button('상관관계 분석하기'):
    #     if len(mul_select) >= 3 :
    #         st.warning('컬럼을 2개만 선택하십시오.')
    #     elif len(mul_select) < 2 :
    #         st.warning('컬럼 2개를 선택하십시오.')
    #     else :
    #         fig2 = plt.figure() 
    #         sns.scatterplot(data = df, x= mul_select[0], y=mul_select[1])  # 3개 이상 선택해도 맨 앞 두 개만 인식함
    #         st.pyplot(fig2)
    #         st.text('{} 컬럼과 {} 컬럼의 상관관계 차트입니다.'.format(mul_select[0],mul_select[1])) 

    # 컬럼 정보 확인
    with st.expander('이 곳을 눌러 컬럼 정보에 대해 알아보세요.'):
        st.text('distance_from_home - 홈으로부터 거래가 발생한 곳과의 거리입니다. (단위 : km)')

        st.text('distance_from_last_transaction - 마지막 거래로부터의 거리입니다. (단위 : km)') 

        st.text('ratio_to_median_purchase_price - 표준 구매 가격 대비 매입 가격 거래 비율입니다.')

        st.text('repeat_retailer - 거래가 동일한 소매점에서 발생하였는지 여부에 대한 컬럼입니다.')

        st.text('used_chip - 칩(신용카드)을 통한 거래인지 여부에 대한 컬럼입니다.')

        st.text('used pinnumber - PIN 번호를 통한 거래인지 여부에 대한 컬럼입니다.')

        st.text('online_order - 온라인 거래인지 여부에 대한 컬럼입니다.')

        st.text('fraud - 거래가 사기성입니다.')  




    