import streamlit as st
from PIL import Image
from datetime import datetime

st.title('大介のアプリ'+datetime.now().strftime("%Y年%m月%d日"))

st.caption('これはテストアプリです')


col1,col2=st.columns(2)
with col1:
    img_btn =st.button("写真")
    if (img_btn) :
        # ローカル画像を表示（同じフォルダに image.png が必要）
        image = Image.open("./data/image.png")
        st.image(image, width=300)

with col2:
    movie_btn =st.button("動画")
    if movie_btn:


        # YouTube動画を埋め込む
        video_url = "https://www.youtube.com/embed/4nsTce1Oce8"  # 埋め込み用のURLに変換
        st.markdown(f"""
            <iframe width="300" src="{video_url}" frameborder="0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)