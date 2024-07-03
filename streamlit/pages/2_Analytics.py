import streamlit as st
import plotly.express as px
import pandas as pd 
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns 
from wordcloud import WordCloud

with open("pages//df.pkl",'rb') as f:

    df=pickle.load(f)

with open("pages//wordcloud_df.pkl",'rb') as f:

          

    wordcloud_df=pickle.load(f)

st.set_page_config(page_title='viz demo')

st.title('Analysis')

new_df=pd.read_csv("pages//data_viz1.csv")


group_df = new_df.pivot_table(index='sector', 
                              values=['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude'], 
                              aggfunc='mean')

st.header('Sector Price Per Sqft Geomap')

fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)

sector=st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

import ast
main = []
def choose_sec(sector):    

    for item in wordcloud_df.query("sector ==sector")['features'].dropna().apply(ast.literal_eval):
        main.extend(item)
        
    return main

feature_text = ' '.join(choose_sec(sector))

plt.rcParams["font.family"] = "Arial"

st.set_option('deprecation.showPyplotGlobalUse', False)
st.header('Features Wordcloud')
wordcloud = WordCloud(width = 800, height = 800, 
                      background_color ='white', 
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud, interpolation='bilinear') 
plt.axis("off") 
plt.tight_layout(pad = 0) 
st.pyplot()


st.header("Area Vs Price")

property_type=st.selectbox('Select Property Type',['flat','house'])

if property_type=='flat':

    fig1 = px.scatter(new_df[new_df['property_type']=='flat'],x="built_up_area", y="price", color="bedRoom" )
    st.plotly_chart(fig1,use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type']=='house'],x="built_up_area", y="price", color="bedRoom" )
    st.plotly_chart(fig1,use_container_width=True)

st.header("BHK Pie Chart")

sector_options=new_df['sector'].unique().tolist()
sector_options.insert(0,'Overall')

selected_sector=st.selectbox("Sector",sector_options)
if selected_sector=='Overall':
    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2,use_container_width=True)

else:
    fig2 = px.pie(new_df[new_df['sector']==selected_sector], names='bedRoom')

    st.plotly_chart(fig2,use_container_width=True)

st.header("Side by side BHK price comparison")

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3,use_container_width=True)

st.header("Distribution plot for  different Property type")

fig4=plt.figure(figsize=(10,4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')

sns.distplot(new_df[new_df['property_type'] == 'flat']['price'],label='flat')
plt.legend()
st.pyplot(fig4)