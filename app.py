import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
fig = go.Figure()

df = pd.read_csv('./data/mydata.csv')

#global variable
url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'

st.title('This is my first webapp!!')

col1, col2 = st.columns((4, 1))
with col1:
    with st.expander('SubContent1'):
        st.subheader('subContent1...')
        st.video(url)

    with st.expander('SubContent2'):
        st.subheader('Image Content...')
        st.image('./images/catdog.jpg')

    with st.expander('SubContent3'):
        st.subheader('HTML Content...')
        import streamlit.components.v1 as htmlviewer
        with open('./htmls/index_copy.html', 'r', encoding = 'UTF-8') as f:
            html1 = f.read()
            f.close()
        htmlviewer.html(html1, height=800, scrolling = True)

    with st.expander('SubContent4'):
        st.subheader('Data App Content...')
        st.table(df)
        st.write(df.describe())
        fig, ax = plt.subplots(figsize = (20, 10))
        df.plot(ax = ax)
        plt.savefig('./images/mygragh.png')
        st.image('./images/mygragh.png')

with col2:
    with st.expander('Tips'):
        st.info('Tips...')