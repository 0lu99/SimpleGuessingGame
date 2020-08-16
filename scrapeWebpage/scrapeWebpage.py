import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

for story_heading in soup.find_all('h2', {'class': 'css-1cmu9py e1voiwgp0'}):
    print(story_heading.text)
