
from tinydb import TinyDB
from os import getcwd
from time import time
import requests
from bs4 import BeautifulSoup
cwd = getcwd()
path = f'{cwd}/backgroundtask/db.json'
db = TinyDB(path)

def isUpdate():
    r = requests.get('https://www.tradingview.com/ideas/forex/?sort=recent&video=no',headers={'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'})
    soup = BeautifulSoup(r.content,'lxml')
    timestamp = soup.find('span',class_='tv-card-stats__time').get('data-timestamp')
    lastbuildtime = db.get(doc_id=1).get('lastbuildtime')
    if timestamp == lastbuildtime:
        db.update({'lastbuildtime':timestamp},doc_ids=[1])
        requests.get('http://0.0.0.0:8000/send')

def download():
    r = requests.get('https://www.tradingview.com/ideas/forex/?sort=recent&video=no')
    soup = BeautifulSoup(r.content,'lxml')
    try:
        widget = soup.find('div',class_='tv-widget-idea js-userlink-popup-anchor')
        currency = widget.find('div',class_='tv-widget-idea__symbol-info').text
        if len(currency) != 6:
            raise Exception('error')
        timeframe = widget.find_all('span',class_='tv-widget-idea__timeframe')[1].text
        signal = widget.find('span',{'dir':'ltr'}).text
        requests.post('http://0.0.0.0:8000/condition',data={'currency':currency,'timeframe':timeframe,'signal':signal})
    except:
        print('something went wrong')

def technical():
    pass

def fundamental():
    pass