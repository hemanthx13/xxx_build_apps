import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Image Display from URL")

# Image URL
url = 'https://picsum.photos/800/600'

# Fetch image from URL
response = requests.get(url)
if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
    st.image(image, caption='Downloaded Image', use_container_width =True)
else:
    st.error("Failed to download image from the URL")
