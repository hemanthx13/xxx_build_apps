import requests
import os

# Image URL from any website
url = 'https://picsum.photos/800/600'  # Free random image API
filename = 'downloaded_image.jpg'

response = requests.get(url)

if response.status_code == 200:
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Image saved as {filename}")
else:
    print("Failed to download image")
