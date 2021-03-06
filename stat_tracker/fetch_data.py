import requests
from bs4 import BeautifulSoup
import re


def fetch(id, mode):
    global site
    if mode == '%unrated':
        game = 'unrated'
    elif mode == '%comp':
        game = 'competitive'
    elif mode == '%sr':
        game = 'spikerush'
    elif mode == '%dm':
        game = 'deathmatch'
    else:
        return None

    #go to website, parse info from body
    stats = [[]]
    id = id.replace(' ', '%20')
    id = id.replace('#', '%23')
    site = 'https://tracker.gg/valorant/profile/riot/'
    site += id + '/overview?playlist=' + game
    res = requests.get(site).text
    soup = BeautifulSoup(res, 'html.parser')
    data = soup.find('body').find_all('div', class_='numbers')

    #store data
    for x in range(len(data)):
        new = []
        new.append(str(data[x].find('span', class_='name')['title']))
        new.append((re.findall('>(.+?)<', str(data[x].find('span', class_='value'))))[0])
        stats.insert(x, new)

    return stats
