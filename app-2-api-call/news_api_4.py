
import os
import requests
from dotenv import load_dotenv

dotenv_path = '../.env'
load_dotenv()
api_key = os.getenv('NEWS_API_KEY')
url = 'https://newsapi.org/v2/top-headlines'

# check samples of GET by going to https://newsapi.org/

params = {
    'country': 'us',   # Fetch news from the US
    'pageSize': 5,     # Limit to 5 news articles
    'apiKey': api_key
}

response = requests.get(url, params=params)

content = response.text
print(content)
