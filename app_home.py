from asyncio import open_connection
import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import streamlit as st
import base64

from app_ml import run_ml

def run_home():
    st.subheader('신용카드 거래 사기 여부 판단해드립니다.')
    st.subheader('데이터 예시')

    #### 이미지 배경으로 만들기
    # @st.cache(allow_output_mutation=True)
    # def get_base64_of_bin_file(bin_file):
    #     with open(bin_file, 'rb') as f:
    #         data = f.read()
    #     return base64.b64encode(data).decode()

    # def set_png_as_page_bg(png_file):
    #     bin_str = get_base64_of_bin_file(png_file)
    #     page_bg_img = '''
    #     <style>
    #     body {
    #     background-image: url("data:image/png;base64,%s");
    #     background-size: cover;
    #     }
    #     </style>
    #     ''' % bin_str
        
    #     st.markdown(page_bg_img, unsafe_allow_html=True)
    #     return

    # set_png_as_page_bg('data/streamlit-app-2022-05-27-15-05-59.gif')


    ### gif 파일 넣기
    """### gif from local file"""
    file_ = open("data/streamlit-app-2022-05-27-17-05-37 (3).gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="Explanation video gif">',
        unsafe_allow_html=True,
    )


    #### 영상넣기
    # st.text('영상 예시')
    # video_file = open('data/streamlit-app-2022-05-27-15-05-59.webm', 'rb')
    # st.video(video_file)
        
