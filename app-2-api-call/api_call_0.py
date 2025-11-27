import requests

url = "https://finance.yahoo.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

request = requests.get(url, headers=headers)
content = request.text
print(content)


# Why the need for headers
'''
When a web browser visits a site, it automatically sends its User-Agent. 
However, when you use a script (like a Python program with the requests library) to fetch a page, 
the default User-Agent is often something generic like "python-requests/2.28.1".

Many websites, especially large, popular ones (like financial sites or social media), 
actively check the User-Agent string and will block requests that appear to come from a simple script or bot.
'''