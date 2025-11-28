'''
Here's the updated Streamlit app with both "Show Body" and "Show Title" buttons:
'''

import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import streamlit.components.v1 as components

st.title("Image & API Data Display")

# Cache the image to prevent reloading
@st.cache_data
def load_image():
    url_image = 'https://picsum.photos/800/600'
    response_image = requests.get(url_image)
    if response_image.status_code == 200:
        return Image.open(BytesIO(response_image.content))
    return None

# Image section - cached so it doesn't reload
st.header("Image from URL")
image = load_image()
if image:
    st.image(image, caption='Downloaded Image', use_container_width=True)
else:
    st.error("Failed to download image")

# API Data section with buttons
st.header("API Data")
api_url = 'https://jsonplaceholder.typicode.com/posts/1'
col1, col2 = st.columns(2)

with col1:
    if st.button("Show Title"):
        response_api = requests.get(api_url)
        if response_api.status_code == 200:
            data = response_api.json()
            title_text = data['title']
            st.markdown("### Post Title")
            st.code(title_text, language='text')

with col2:
    if st.button("Show Body"):
        response_api = requests.get(api_url)
        if response_api.status_code == 200:
            data = response_api.json()
            body_text = data['body']
            st.markdown("### Post Body")
            st.code(body_text, language='text')
