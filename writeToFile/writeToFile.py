import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

filename = input("What file do you want to write to?: ")

with open(filename, 'w') as open_file:
    for story_heading in soup.find_all('h2', {'class': 'css-1cmu9py e1voiwgp0'}):
        open_file.write(story_heading.text)
