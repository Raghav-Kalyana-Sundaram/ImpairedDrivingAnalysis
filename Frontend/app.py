#https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
import streamlit as st
import time
import numpy as np

st.title("Impaired Driving Analysis") 
st.subheader("Graphs and Analysis") 

st.image('G:\My Drive\ImpairedDrivingAnalysis\Frontend\Images\Image1.jpg')

with st.sidebar:
    st.radio ('Select one' , [1,2]) 

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")

st.file_uploader('Upload a photo you want to test') 

with st.form(key='form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login') 
