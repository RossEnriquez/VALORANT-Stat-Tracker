import requests
import bs4
import re

def fetch(id, mode):
    global site
    if mode == 'Unrated':
        game = 'unrated'
    elif mode == 'Competitive':
        game = 'competitive'
    elif mode == 'Spike Rush':
        game = 'spikerush'
    elif mode == 'Deathmatch':
        game = 'deathmatch'
    else:
        return None

    #go to website, parse info from body
    stats = [[]]
    id = id.replace(' ', '%20')
    id = id.replace('#', '%23')
    site = 'https://tracker.gg/valorant/profile/riot/'
    site += id + '/overview?playlist=' + game
    res = requests.get(site)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    data = soup.find('body').find_all('div', class_= 'numbers')

    #store data
    for x in range(len(data)):
        new = []
        new.append(str(data[x].find('span', class_='name')['title']))
        new.append((re.findall('>(.+?)<', str(data[x].find('span', class_='value'))))[0])
        stats.insert(x, new)

    return stats