#https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
import streamlit as st
import time
import numpy as np
from PIL import Image
import requests
import shutil


st.title('Impaired Driving Reduction') 
st.subheader('Paste links to different images of drivers around the world to see if they could be impaired') 
image=Image.open('Jonny-Bairstow-batting-semifinal-match-England-Australia-2019.webp')
st.image(image, caption='Bairstow') 
image_url=st.text_area('Paste the link to the image here', value='Please make sure the image is free for commercial use and does not require any attribution', height=25, max_chars=100)