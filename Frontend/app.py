#https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
import streamlit as st
import time
import numpy as np

st.title("Impaired Driving Analysis") 
st.subheader("Graphs and Analysis") 
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

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
