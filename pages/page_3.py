import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import datetime


df=pd.read_csv('./data/月別_温度湿度デモデータ.csv',index_col='月')

st.dataframe(df)
st.table(df)

st.line_chart(df)

st.bar_chart(df["平均湿度（％）"])