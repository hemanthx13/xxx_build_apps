'''
Here's the updated Streamlit app with a button to show the body data only when pressed:
'''
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Image & API Data Display")

# Image section

st.header("Image from URL")
url_image = 'https://picsum.photos/800/600'
response_image = requests.get(url_image)
if response_image.status_code == 200:
    image = Image.open(BytesIO(response_image.content))
    st.image(image, caption='Downloaded Image', use_container_width=True)
else:
    st.error("Failed to download image")

# API Data section with button
st.header("API Data (Body Only)")
api_url = 'https://jsonplaceholder.typicode.com/posts/1'

if st.button("Show Body"):
    response_api = requests.get(api_url)
    if response_api.status_code == 200:
        data = response_api.json()
        body_text = data['body']

        # Display body in a nice box
        st.markdown("### Post Body")
        st.code(body_text, language='text')
    else:
        st.error("Failed to fetch API data")
else:
    st.info("Click 'Show Body' button to display the post content")
