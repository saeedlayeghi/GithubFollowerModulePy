import requests
from bs4 import BeautifulSoup
import asyncio, random

header = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
    'Connection': 'keep-alive'
}

async def run(*,urlquery):
    proxies = open('proxies.txt','r')
    try:
        res = requests.get(f'https://github.com/{urlquery}', headers=header, proxies={'http': f'{random.choice(proxies.readlines())}'}, timeout=20)
    except:
        sys.exit('Cannot connect | Baglanti Kurulamadi | Kan niet verbinden')
    finally:
        proxies.close()

    try:
        response = res.status_code
        webdata = res.text
    except:
        sys.exit('Cannot connect | Baglanti Kurulamadi | Kan niet verbinden')
    finally:
        proxies.close()

    if response == 200:
        scrapeinfo = BeautifulSoup(webdata,'html.parser')
        vidmolyobj = scrapeinfo.find('span', class_='text-bold color-fg-default').prettify().split('\n')
        
        githubfollowers = vidmolyobj[1].strip(' ')

        return print("{}".format(githubfollowers))
    else:
        proxies.close()
        sys.exit('Cannot connect | Baglanti Kurulamadi | Kan niet verbinden')

