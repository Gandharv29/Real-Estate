import streamlit as st 
import pickle
import pandas as pd
import numpy as np 

st.set_page_config(page_title='viz demo')
st.title('Price Prediction')
with open("pages//df.pkl",'rb') as f:

    df=pickle.load(f)

with open("pages//pipeline.pkl",'rb') as f:

    pipeline=pickle.load(f)


st.header('Enter Your Inputs')

property_type=st.selectbox("Property Type",['flat','house'])

sector=st.selectbox('Sector',sorted(df['sector'].unique().tolist()))
bedroom=float(st.selectbox('Number of Bedrooms',sorted(df['bedRoom'].unique().tolist())))
bathroom=float(st.selectbox('Number of  Bathrooms',sorted(df['bathroom'].unique().tolist())))

balcony=st.selectbox('Number of  Balconies',sorted(df['balcony'].unique().tolist()))

age_possesion=st.selectbox('Property age',sorted(df['agePossession'].unique().tolist()))
furnish_type=st.selectbox('Furninshing Type',sorted(df['furnishing_type'].unique().tolist()))
luxury=st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))
floor_category=st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))


builtup_area=bathroom=float(st.number_input('Builtup area'))

servant_room=float(st.selectbox('Servant Room',[0.0,1.0]))
store_room=float(st.selectbox('Store Room',[0.0,1.0]))

if st.button('Predict'):
    data = [[property_type, sector, bedroom, bathroom, balcony, age_possesion, builtup_area, servant_room, store_room, furnish_type, luxury, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)


    base_price=np.expm1(pipeline.predict(one_df))[0]
    low=base_price - 0.22
    high=base_price + 0.22

    st.text(f'the price of the property is between {round(low,2)}Cr. and {round(high,2)}Cr.')
