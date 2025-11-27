import requests

# Define the API endpoint URL
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Make a GET request to the API
response = requests.get(url)

# Check if the response status code indicates success
if response.status_code == 200:
    # Parse the JSON response content
    data = response.json()
    # Print the data retrieved
    print("Post ID:", data['id'])
    print("Title:", data['title'])
    print("Body:", data['body'])
else:
    print("Failed to retrieve data:", response.status_code)
