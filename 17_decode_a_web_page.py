import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

for heading in soup.find_all(["h1", "h2", "h3"]):
    text = heading.get_text(strip=True)

    if text:
        print(text)
