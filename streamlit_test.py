from re import sub
from turtle import width
import streamlit as st
import datetime
from PIL import Image

st.title('おれおれアプリ')
st.caption('これはテストアプリですよ')

col1,col2 = st.columns(2)

with col1:
    st.subheader('自己紹介')
    st.text('こんばんはー\nよろろろろろろろ')
    code ='''
    import streamlit as st

    なんてな
    '''
    st.code(code,language='python')

    with st.form(key='prof1'):
        # TEXT BOX
        name1 = st.text_input('name1')
        name2 = st.text_input('name2')

        # selectbox
        age_category = st.selectbox(
            '年齢層',
            ('0-17','18-24','25-36','37-50','50-64','65-')
        )

        # radio
        radio_select = st.radio(
            '選択',
            ('0-17','18-24','25-36','37-50','50-64','65-')
        )

        # multiselect
        multi_select = st.multiselect(
            '複数',
            ('0-17','18-24','25-36','37-50','50-64','65-')
        )

        # slider
        height = st.slider('範囲',min_value=0,max_value=255)

        # date
        st_date = st.date_input(
            '開始日',
            datetime.date(2022,8,30)
        )

        # color
        color = st.color_picker('picker','#A0F0CC')


        submit_btn = st.form_submit_button("送信")
        cancel_btn = st.form_submit_button("キャンセル")
        if submit_btn:
            st.text(f'ようこそ！ {name1} {name2}')
            st.text(f'{age_category}')

with col2:
    st.text('konnnakannji')
    image = Image.open('data/udonya_box.gif')
    st.image(image)