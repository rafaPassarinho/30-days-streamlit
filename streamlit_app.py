import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

from datetime import datetime, time

st.header('st.button')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.header('st.write')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

st.write('Bellow is a DataFrame:', df,'Above is a DataFrame.')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.write(c)

st.header('st.slider')
st.subheader('Slides')

age = st.slider('How old are you?', 0, 130, 25)

st.subheader('Range slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
st.write('Values:', values)

st.subheader('Range time slider')

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)

st.subheader('Datetime slider')
start_time = st.slider(
    'When do you start?',
    value=datetime(2020, 1, 1, 12, 30),
    format='DD/MM/YY - hh:mm'
)
st.write('Start time:', start_time)

st.header('Line chart')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    ['Red', 'Green', 'Blue']
)
st.write('Your favorite color is:', option)

st.header('st.multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)
st.write('You selected:', options)

st.header('st.checkbox')
st.write('What would you like to order?')
icecream = st.checkbox('Ice Cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('cola')
if icecream:
    st.write('Great! Here is some more 🍦')
if coffee:
    st.write('Great! Here is some more ☕')
if cola:
    st.write('Great! Here is some more 🥤')



st.header('st.latex')
st.latex(r'''
f(x) = x^2
''')

st.title('st.file_uploader')
st.subheader('Input CSV')
uploaded_file = st.file_uploader('Choose a parquet file', type='parquet')

if uploaded_file is not None:
    df = pd.read_parquet(uploaded_file)
    st.subheader('Dataframe')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
else:
    st.info('👆 Upload a PARQUET file')
