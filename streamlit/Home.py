import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("Welcome to Gurgaon Property Service! 👋")

st.sidebar.success("Select a module above.")


st.title('What are the services offered?')

st.header('Property Price Prediction')
st.write("""Our property price prediction tool allows users to input their desired property 
features, such as location, size, and amenities. Based on these inputs, the system 
provides an estimated price for properties in Gurgaon. This helps users make informed 
decisions by giving them a realistic expectation of the market value for properties 
that match their preferences.""")

st.header('Visual Analysis')
st.write("""Explore the real estate market in Gurgaon with our visual analysis feature.
We provide comprehensive graphs and interactive visualizations that display the 
distribution of properties across various neighborhoods in Gurgaon.
These visual insights help users understand market trends, property hotspots, and 
investment opportunities at a glance.""")

st.header('Recommendation System')
st.write("""Our recommendation system is designed to simplify the property search process.
By analyzing user preferences and past behavior,it suggests properties that best 
match the users criteria.Whether you’re looking for a new home or an investment
opportunity,our recommendation system helps you find the perfect property 
quickly and efficiently.""")