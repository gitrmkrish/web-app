import pandas as pd
import streamlit as st
import pickle

cars_df = pd.read_csv("https://raw.githubusercontent.com/gitrmkrish/web-app/main/cars24-car-price.csv")



encode_dict = {'fuel_type': {
    'petrol': 1,
    'gas': 2,
    'diesel': 3,
    'carbon': 4
}, 'transmission_type': {
    'Manual': 1,
    'Automatic': 2
}, 'seller_type': {
    'Individual': 1,
    'Dealer': 2
}, 'seats': {
    '4': 4,
    '5': 5,
    '9': 9,
    '11': 11
}}

st.write('dataset')

st.dataframe(cars_df)
#inputss
col1, col2 = st.columns(2)

fuel_type_value = col1.selectbox('select the fuel type',['petrol' , 'gas','diesel','carbon'])

engine_value = col2.slider('select the engine power', 500 , 5000 , step = 100)

transmission_type_value  = col2.selectbox('select the transmission type',['Manual','Automatic'])

seats_value = col2.selectbox('select the seats',['4','5','9','11'])

seller_type_value = col2.selectbox('select the seller type',['Individual','Dealer'])

# need a button my model is called and data is passed in model and prediction is done
# get data from user and encode it as dict
fuel_type_encoded = encode_dict['fuel_type'][fuel_type_value]
transmission_type_encoded = encode_dict['transmission_type'][transmission_type_value]
seller_type_encoded = encode_dict['seller_type'][seller_type_value]
seats_encoded = encode_dict['seats'][seats_value]


def model_pred(seller_type_value ,fuel_type_value, transmission_type_value, seats_value):
        with open('car_pred' ,"rb") as file:
            reg_model = pickle.load(file)
            input_fea  = [[2012,seller_type_encoded,120000,fuel_type_encoded,transmission_type_encoded,19.7,796,46.3,seats_encoded]]
            return reg_model.predict(input_fea)

if st.button('predict price'):
    price = model_pred(fuel_type_value, engine_value , transmission_type_value , seats_value)
    st.text(price)