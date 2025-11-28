'''
Here's the updated code that prevents the image from refreshing when buttons are clicked
by using Streamlit's @st.cache_data decorator
'''
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Image & API Data Display")

# Cached image function to prevent refresh
@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    return None

# Image section - cached so it doesn't reload
st.header("Image from URL")
url_image = 'https://picsum.photos/800/600'
image = load_image(url_image)
if image:
    st.image(image, caption='Downloaded Image', use_container_width=True)
else:
    st.error("Failed to download image")

# API Data section with button
st.header("API Data")
api_url = 'https://jsonplaceholder.typicode.com/posts/1'

if st.button("Show Body"):
    response_api = requests.get(api_url)
    if response_api.status_code == 200:
        data = response_api.json()
        body_text = data['body']
        st.markdown("### Post Body")
        st.code(body_text, language='text')
    else:
        st.error("Failed to fetch API data")
else:
    st.info("Click 'Show Body' button to display the post content")
