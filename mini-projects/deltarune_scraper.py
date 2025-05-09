"""
For legal reasons this is a project solely for educational purposes that will not be used.
"""

import requests
from bs4 import BeautifulSoup
from pathlib import Path

response = requests.get("https://archive.org/details/deltaruneost/")
text = response.text

soup = BeautifulSoup(text, features="html.parser")

links = soup.find_all("link", itemprop="associatedMedia")


filtered_links = [link for link in links if link["href"].endswith(".m4a") or link["href"].endswith(".mp3")]


names = soup.find_all("meta", itemprop="name")


for i in range(0,len(names)):
    link = filtered_links[i]
    name = names[i]
    piracy = requests.get(link["href"])
    content = piracy.content
    if link["href"].endswith(".m4a"):
        ext = ".m4a"
    elif link["href"].endswith(".mp3"):
        ext = ".mp3"
    with open(Path.home() / f"Music/Deltarune/{name["content"]}{ext}","wb") as file:
        file.write(content)
