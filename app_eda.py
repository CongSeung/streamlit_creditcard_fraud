import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
from fbprophet import Prophet
import streamlit as st

################ 차트 한글 안 깨지게
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

#########################################

def run_eda():
    st.text('과거 데이터를 분석해보자.')
    
    df = pd.read_csv('data/card_transdata.csv')
    
    st.subheader('머신러닝 학습에 사용된 데이터셋')

   

    my_order = ['데이터셋 보기', '기본 통계자료 보기']   

    status = st.sidebar.radio('자료 선택', my_order)  # 라디오 버튼은 1과 0이 아닌 들어가 있는 값을 띄게 된다.

    if status == my_order[0] :
        st.dataframe(df)
    elif status == my_order[1] :
        st.dataframe(df.describe())

    select = st.sidebar.selectbox('히스토그램 확인하기', df.columns.to_list())
    
    if st.sidebar.button('히스토그램 확인하기'):
        fig1 = plt.figure() 
        sns.countplot(data = df , x = select)
        st.pyplot(fig1)
    mul_select = st.sidebar.multiselect('상관관계 분석 / 컬럼 2개 선택',df.columns.to_list())

    if st.sidebar.button('상관관계 분석하기'):
        if len(mul_select) >= 3 :
            st.warning('컬럼을 2개만 선택하십시오.')
        else :
            fig2 = plt.figure() 
            sns.scatterplot(data = df, x= mul_select[0], y=mul_select[1])  # 3개 이상 선택해도 맨 앞 두 개만 인식함
            st.pyplot(fig2)
            st.text('{} 컬럼과 {} 컬럼의 상관관계 차트입니다.'.format(mul_select[0],mul_select[1])) 

    with st.expander('이 곳을 눌러 컬럼 정보에 대해 알아보세요.'):
        st.text('distance_from_home - 홈으로부터 거래가 발생한 곳과의 거리입니다. (단위 : km)')

        st.text('distance_from_last_transaction - 마지막 거래로부터의 거리입니다. (단위 : km)') 

        st.text('ratio_to_median_purchase_price - 표준 구매 가격 대비 매입 가격 거래 비율입니다.')

        st.text('repeat_retailer - 거래가 동일한 소매점에서 발생하였는지 여부에 대한 컬럼입니다.')

        st.text('used_chip - 칩(신용카드)을 통한 거래인지 여부에 대한 컬럼입니다.')

        st.text('used pinnumber - PIN 번호를 통한 거래인지 여부에 대한 컬럼입니다.')

        st.text('online_order - 온라인 거래인지 여부에 대한 컬럼입니다.')

        st.text('fraud - 거래가 사기성입니다.')  

    
    