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

