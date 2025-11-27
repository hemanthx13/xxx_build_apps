import requests

url = 'https://newsapi.org/v2/top-headlines?country=us&pageSize=5&category=business&apiKey=a5ffbfe368c44488b1701bcdf8d5bb92'

response = requests.get(url)

#content = response.text
content = response.json()
#print(content)
print(content["articles"])