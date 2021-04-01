from random import randint
import pandas as pd                                   
from bs4 import BeautifulSoup                          
import requests  
import datetime
from time import sleep
import random
from itertools import cycle
import traceback
import deathbycaptcha
import deathbycaptcha
import json

# Put the proxy and reCaptcha token data

df1 = pd.read_excel('data.xlsx')
all_links = df1['links'].tolist()
# # print(all_links)
data = []
list = {}
counter = 0
from scraper_api import ScraperAPIClient
client = ScraperAPIClient("d3f449467240af8dd030d344a711ea0b")

# result = client.get(url = 'http://httpbin.org/ip').text
# print(result)

for url in all_links[:1]:
    print(url)
    
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.749 Yowser/2.5 Safari/537.36'
    ]
    user_agent = random.choice(user_agent_list)
   
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': user_agent
    }
    result = requests.get(url,headers = headers,timeout= 5)
    # print(result)
    sleep(randint(4,7))
    soup = BeautifulSoup(result.content, 'html5lib')
    # print(r.content)


    try:
        min = soup.find('span',attrs= {'class':'js-label js-price _itL _ibU _ibV _idj _mo2'}).get_text()
        print(min)
    except:
        min = '-'



    print(min)
    
    list = {
        'Links' : url,
        'Cheepest price': min
    }
    data.append(list)
df = pd.DataFrame(data)
df.to_excel(f'Cheepest_price.xlsx',encoding='utf-8-sig', index=False)