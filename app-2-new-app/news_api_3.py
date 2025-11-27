import os
import requests

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('NEWS_API_KEY')
#api_key = 'a5ffbfe368c44488b1701bcdf8d5bb92'  # Get your free key from newsapi.org
url = 'https://newsapi.org/v2/top-headlines'
params = {
    'country': 'us',   # Fetch news from the US
    'pageSize': 5,     # Limit to 5 news articles
    'apiKey': api_key
}

response = requests.get(url, params=params)

if response.status_code == 200:
    news = response.json()
    for article in news['articles']:
        print('Title:', article['title'])
        print('Description:', article['description'])
        print('URL:', article['url'])
        print('---')
else:
    print('Failed to fetch news:', response.status_code)
