# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup


url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'


header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

data = requests.get(url,headers=header).text
soup = BeautifulSoup(data,'html.parser')

rates = soup.find(id='exchangeRate')

tbody = rates.find('tbody')

trs = tbody.find_all('tr')[1:]


for row in trs:
    tds = row.find_all('td',recursive=False)
    if len(tds) == 4:
        
        print(tds[0].text.strip().split()[0])
        print(tds[1].text.strip())
        print(tds[2].text.strip())
        print(tds[3].text.strip())
        print()
    
    


    
