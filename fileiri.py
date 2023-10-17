import streamlit as st

st.header('Calculating your worth ', divider='rainbow')

def pay_monthly (hours:float, rate:float):
    return hours*rate

name = st.text_input ('What is your name: ')
hours = st.number_input ('How many hours did you work:  ')
rate = st.number_input ('How much do you get paid per hour: ', step = 1)
pay = pay_monthly (hours,rate)

if st.button('Calculate wage!'):
    st.write(name, "Your wage is",pay)
