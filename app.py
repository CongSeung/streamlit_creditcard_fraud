import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import random
import seaborn as sns
import streamlit as st

from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml


def main():
    
    st.title("Determination of Fraud")

    menu = ['Home', 'Data EDA' ,'Determination of Fraud']

    choice = st.sidebar.selectbox('메 뉴 선 택', menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()


if __name__ == '__main__':
    main()