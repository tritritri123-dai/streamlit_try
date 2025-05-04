import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import datetime

if 'name' not in st.session_state:
    st.session_state.name = ''
    st.session_state.address = ''
    st.session_state.age_category = '大人(18歳以上)'
    st.session_state.gender_category = '回答しない'
    st.session_state.hobby = []
    st.session_state.checked = False
    st.session_state.reset_triggered = False  # ← 追加

# --- フォーム表示 ---
with st.form(key='profile_form'):
    name = st.text_input('名前', value=st.session_state.name)
    address = st.text_input('住所', value=st.session_state.address)
    age_options = ['', '子ども(18歳未満)', '大人(18歳以上)']
    age_category = st.selectbox('年齢層別', age_options, index=age_options.index(st.session_state.age_category))
    gender_options = ['男', '女', '回答しない']
    gender_category = st.radio('性別', gender_options, index=gender_options.index(st.session_state.gender_category))
    hobby = st.multiselect('趣味', ['野球', '柔道', '剣道'], default=st.session_state.hobby)
    height=st.slider('身長',min_value=100,max_value=200)
    start_date=st.date_input('開始日',datetime.date(2022,7,1))
    color =st.color_picker('テーマカラー','#ff0000')


    check_btn = st.form_submit_button("入力内容確認")
    cancel_btn = st.form_submit_button("キャンセル")
    
    if check_btn:
        st.session_state.name = name
        st.session_state.address = address
        st.session_state.age_category = age_category
        st.session_state.gender_category = gender_category
        st.session_state.hobby = hobby
        st.session_state.checked = True
        


        st.experimental_set_query_params(reset="true")
        st.rerun()
        

    if cancel_btn:
        # セッション変数をリセット
        st.session_state.name = ''
        st.session_state.address = ''
        st.session_state.age_category = '大人(18歳以上)'
        st.session_state.gender_category = '回答しない'
        st.session_state.hobby = []
        st.session_state.checked = False
        st.session_state.reset_triggered = True  # ← フラグを立てる

# --- キャンセル処理の rerun をフォームの外で実行 ---
if st.session_state.reset_triggered:
    st.session_state.reset_triggered = False  # すぐリセット
    st.rerun()

# --- 確認画面 ---
if st.session_state.get('checked', False):
    user_data = {
        '項目': ['名前', '住所', '年齢層', '性別', '趣味'],
        '入力内容': [
            st.session_state.name,
            st.session_state.address,
            st.session_state.age_category,
            st.session_state.gender_category,
            ', '.join(st.session_state.hobby)
        ]
    }
    df = pd.DataFrame(user_data)
    df.index = [''] * len(df)
    st.write("【内容の確認】")
    st.table(df)
    if st.button("送付"):
        st.success("送付が完了しました！")
        st.session_state.checked = False
