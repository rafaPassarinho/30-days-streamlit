import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

from time import sleep
from time import time as t
from datetime import datetime, time

st.set_page_config(
    page_title="Streamlit Demo",
    layout="wide")


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

st.title('How to layout your Streamlit app')
with st.expander('About this app'):
    st.write('This app is a demonstration of how to layout your Streamlit app.')
    st.image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fflxt.tmsimg.com%2Fassets%2Fp8741188_b_v10_aa.jpg&f=1&nofb=1&ipt=2d342b6e68c8c493a73fb03947f1e73ba980d3cdc7e89ff1449a8c230d2d7a05&ipo=images', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Pick an emoji', ['', '🎈', '🦄', '🍉'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Pizza', 'Ice Cream', 'Salad'])

st.header('Output')
col1, col2, col3 = st.columns(3)

with col1:
    if user_name != '':
        st.write(f'👋 Hello {user_name}!')
    else:
        st.write('👈  Please enter your **name**!')
with col2:
    if user_emoji != '':
        st.write(f'{user_emoji} is your favorite **emoji**!')
    else:
        st.write('👈  Please select an **emoji**!')
with col3:
    if user_food != '':
        st.write(f'You like **{user_food}**!')
    else:
        st.write('👈  Please select your favorite **food**!')

st.title('st.progress')

with st.expander('About progress bars'):
    st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
    sleep(0.1)
    my_bar.progress(percent_complete + 1)

st.balloons()

st.title('st.form')
st.header('Planilha Financeira')

with st.form(key='my_form'):
    st.subheader('Insira os valores iniciais para o **cálculo financeiro**.')
    saldo_inicial = st.number_input('Qual é o **saldo inicial**?', value=1000)
    diario = st.number_input('Qual é o **gasto diário**?', value=30)
    dia_salario = st.number_input('Qual é o **dia do salário**?', value=30)
    salario = st.number_input('Qual é o **valor do salário**?', value=1000)
    submit_button = st.form_submit_button(label='Criar Planilha')

if submit_button:
    st.markdown(f'''
                ## **Planilha Financeira**
                ### Saldo inicial: R$ {saldo_inicial}
                ### Gasto diário: R$ {diario}
                ### Dia do salário: {dia_salario}
                ### Valor do salário: R$ {salario}
                ''')
else:
    st.info('👆 Clique no botão para criar a planilha.')

st.title('st.cache_data')
a0 = t()
st.subheader('Using st.cache_data')

@st.cache_data()
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2_000_000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

st.write(load_data_a())
a1 = t()
st.info(f'Tempo de execução: {a1 - a0:.2f} segundos')

b0 = t()
st.subheader('Without st.cache_data')

def load_data_b():
    df = pd.DataFrame(
        np.random.rand(2_000_000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

st.write(load_data_b())
b1 = t()
st.info(f'Tempo de execução: {b1 - b0:.2f} segundos')

st.title('st.session_state')

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs / 2.20462
def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg * 2.20462

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)