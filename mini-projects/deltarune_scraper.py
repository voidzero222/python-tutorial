import requests
from bs4 import BeautifulSoup

response = requests.get("https://archive.org/details/deltaruneost/")
text = response.text

soup = BeautifulSoup(text, features="html.parser")

links = soup.find_all("link", itemprop="associatedMedia")

[print(link) for link in links]
