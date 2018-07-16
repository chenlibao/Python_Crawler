import time
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
song3 = client.kugou3_db.song3
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

def get_info(url):
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    ranks = soup.select('.pc_temp_num')
    titles = soup.select('.pc_temp_songname')
    times = soup.select('.pc_temp_time')
    # for rank in ranks:
    #     rank = rank.get_text().strip()
    #     rank_id = song3.insert(rank)
    for rank,title,time in zip(ranks,titles,times):
        data = {
            'rank':rank.get_text().strip(),
            'singer':title.get_text().split('-')[0].strip(),
            'song':title.get_text().split('-')[1].strip(),
            'time':time.get_text().strip()
        }
        song3_id = song3.insert(data)


if __name__ == "__main__":
    urls = {'http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1,24)}
    for url in urls:
        get_info(url)
        time.sleep(1)