from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests
import os
import subprocess

file = open('likes.txt', 'r')

likes = (file.read()).split(os.linesep)

for like in likes:
    
    link = 'https://www.youtube.com/results?search_query='\
        + quote_plus(like)
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    link = soup.find_all('a',attrs={'class':'yt-uix-tile-link'})[0].get('href')
    link = 'https://www.youtube.com' + link
    subprocess.Popen(['youtube-dl', '-f', '140', link])