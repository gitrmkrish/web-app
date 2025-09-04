import streamlit as st

st.header(" Hi I am Muralikrishnan and I am sooo :blue[cool] :sunglasses:")

st.badge(" my first web app")

st.write("Data Scientist")

import pandas as pd
df = pd.read_csv(r'C:\Users\HP\OneDrive\Documents\GitHub\web-app\cars24-car-price.csv')


st.write(df)

agree = st.checkbox(" am I awesome?")

if agree:
    st.write("Great!")

    st.button("Reset", type="primary")
    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")

    if st.button("Aloha", type="tertiary"):
        st.write("Ciao")