#https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
import streamlit as st
import time
import pandas as pd
import numpy as np
from PIL import Image

st.title("Impaired Driving Analysis") 

#image1=Image.open('Graph1.jpg')
#st.image(image1,caption='Our first graph showing how the accuracy of our model increased as we tested it more times')

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.

st.download_button('Download the model','    ', file_name='Impaired Driving Machine Learning Model.h5') 

df=pd.DataFrame(np.random.randn(800,2)/[50,50]+[46.34, -108.70], columns=['latitude', 'longitude']) 
st.map(df)

with st.form(key='form'):
    username = st.text_input('ID')
    password = st.text_input('ZIP Code')
    st.form_submit_button('Submit:') 
    
  
