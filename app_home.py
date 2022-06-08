from asyncio import open_connection
import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import streamlit as st
import base64


def run_home():
    st.subheader('신용카드 거래 사기 여부 판단해드립니다.')
    st.text('좌측 메뉴를 통해 데이터를 탐색해보고, 카드 결제건에 대해 사기 여부를 알 수 있습니다.')
    st.text(' ')

    st.text('금융민원관련 상담전화, 국번없이 1332')
    st.write("금융감독원 [바로가기](https://www.fss.or.kr)")

    ### gif 파일 넣기
    """### gif from local file"""
    file_ = open("data/streamlit-app-2022-06-02-16-06-72 (2).gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="Explanation video gif">',
        unsafe_allow_html=True,
    )

