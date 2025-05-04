import streamlit as st

code = '''
import pandas as pd
# これはテストの画面として現れているものです。
# これはもしかして
# もしかして
# もし
# も・・・・
# 。。。。。。。
# 返事がない。ただのしかばねのようだ。
# codeで使うとコピーができるみたいだね。これは覚えておきたい。
'''

st.code(code, language='python')
